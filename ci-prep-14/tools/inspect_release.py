"""Read-only structural preflight for an existing J.A.R.V.I.S. update ZIP.

This checks ZIP paths and basic integrity, NOT publisher signatures.
It never installs, extracts, signs, uploads, or executes archive content.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from pathlib import PurePosixPath
import re
import stat
import sys
import zipfile

MAX_ENTRIES = 4000
MAX_FILE = 80 * 1024 * 1024
MAX_TOTAL = 300 * 1024 * 1024
MAX_ARCHIVE = 160 * 1024 * 1024
MAX_RATIO = 500
DRIVE = re.compile(r"^[A-Za-z]:")
RESERVED = re.compile(r"^(?:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?$", re.I)


def sha256_stream(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def safe_name(name: str) -> bool:
    if (not name or len(name) > 300 or name.startswith(("/", "\\"))
            or DRIVE.match(name) or "\\" in name or ":" in name or "\x00" in name
            or any(ord(char) < 32 for char in name)):
        return False
    parts = name.split("/")
    if any(not p or p in (".", "..") or p.endswith((".", " ")) or RESERVED.match(p) for p in parts):
        return False
    return PurePosixPath(name).as_posix() == name


def inspect_release_archive(zip_path: Path) -> dict:
    zip_path = Path(zip_path)
    if zip_path.stat().st_size > MAX_ARCHIVE:
        raise ValueError("ZIP exceeds maximum compressed size")
    seen = set()
    bytes_total = 0
    num = 0
    with zipfile.ZipFile(zip_path, "r") as archive:
        for info in archive.infolist():
            num += 1
            name = info.filename
            if num > MAX_ENTRIES:
                raise ValueError("Too many entries")
            if not safe_name(name) or info.is_dir():
                raise ValueError("Unsafe ZIP path")
            key = name.casefold()
            if key in seen:
                raise ValueError("Duplicate or case-colliding ZIP entry")
            seen.add(key)
            mode = (info.external_attr >> 16) & 0xFFFF
            if info.create_system == 3 and stat.S_IFMT(mode) not in (0, stat.S_IFREG):
                raise ValueError("ZIP contains symlink or special file")
            if info.flag_bits & 1:
                raise ValueError("Encrypted archive entry")
            if info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
                raise ValueError("Unsupported compression")
            if info.file_size > MAX_FILE:
                raise ValueError("Oversized archive entry")
            bytes_total += info.file_size
            if bytes_total > MAX_TOTAL:
                raise ValueError("Archive expands beyond size limit")
            if info.file_size and (info.compress_size == 0 or info.file_size / info.compress_size > MAX_RATIO):
                raise ValueError("Unreasonable ZIP compression ratio")
            # Read compressed data fully and check CRC, without extracting to disk.
            with archive.open(info) as src:
                while src.read(1024 * 1024):
                    pass
    return {
        "status": "ZIP_STRUCTURE_ONLY_PASSED__SIGNATURE_NOT_CHECKED",
        "zip_sha256": sha256_stream(zip_path),
        "entry_count": num,
        "uncompressed_bytes": bytes_total,
        "signature_checked": False,
        "publisher_trust_verified": False,
    }


def read_public_manifest_summary(path: Path) -> dict:
    if path.stat().st_size > 1024 * 1024:
        raise ValueError("Manifest too large")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise ValueError("Manifest must be an object")
    # Do not print credentials, opaque signatures, or sensitive values.
    return {"json_valid": True, "top_level_fields": sorted(obj.keys()),
            "version": obj.get("version") if isinstance(obj.get("version"), str) else None,
            "signature_checked": False}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("zip_file", type=Path)
    p.add_argument("--manifest", type=Path)
    args = p.parse_args()
    report = {"archive": inspect_release_archive(args.zip_file)}
    if args.manifest:
        report["manifest"] = read_public_manifest_summary(args.manifest)
    report["warning"] = "Read-only preflight. A valid RSA signature is still mandatory for update installation."
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, json.JSONDecodeError, zipfile.BadZipFile, zipfile.LargeZipFile, RuntimeError) as exc:
        print("RELEASE ZIP ABGELEHNT: " + str(exc), file=sys.stderr)
        raise SystemExit(1)
