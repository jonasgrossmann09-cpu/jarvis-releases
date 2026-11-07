# -*- coding: utf-8 -*-
"""Minimaler Tagebuch-Link-Patch fuer J.A.R.V.I.S.

Auf einer Kopie oder bei geschlossener App anwenden. Danach muss der
vorhandene Releaseprozess ein signiertes Update daraus erzeugen.
"""
from __future__ import annotations

import argparse
import ast
from datetime import datetime
import os
from pathlib import Path
import re
import shutil
import tempfile

DIARY_URL = 'http://127.0.0.1:18767/'
TARGET = 'jarvis_modern_ui.py'
OLD_CALLBACK = re.compile(r"lambda\s*:\s*_launch\s*\(\s*self\s*,\s*(['\"])Tagebuch\1\s*\)")
NEW_CALLBACK = "lambda:__import__('webbrowser').open('http://127.0.0.1:18767/', new=2)"


def patch_text(source: str) -> tuple[str, str]:
    """Return (code, status). Unbekannte Layouts nicht veraendern."""
    matches = list(OLD_CALLBACK.finditer(source))
    if not matches:
        if source.count(NEW_CALLBACK) == 1:
            ast.parse(source, filename=TARGET)
            return source, 'already'
        raise ValueError('Tagebuch-Kachel nicht eindeutig erkannt; keine Aenderung')
    if len(matches) != 1 or NEW_CALLBACK in source:
        raise ValueError('Mehrdeutiger Tagebuch-Aufruf; keine Aenderung')
    changed = OLD_CALLBACK.sub(lambda _: NEW_CALLBACK, source)
    ast.parse(changed, filename=TARGET)
    return changed, 'patched'


def apply(folder: Path) -> tuple[str, str | None]:
    folder = folder.resolve(strict=True)
    target = folder / TARGET
    if not (folder / 'jarvis.py').is_file() or not target.is_file():
        raise ValueError('jarvis.py oder jarvis_modern_ui.py fehlt')
    if target.is_symlink():
        raise ValueError('Symbolischer Link als UI-Datei nicht erlaubt')
    raw = target.read_bytes()
    original = raw.decode('utf-8-sig')
    modified, status = patch_text(original)
    if status == 'already':
        return 'already', None
    backup_dir = folder / '.tagebuch-patch-backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup_dir.mkdir(parents=True, exist_ok=False)
    backup = backup_dir / TARGET
    shutil.copy2(target, backup)
    fd, tmp = tempfile.mkstemp(prefix='.tagebuch-', suffix='.tmp', dir=folder)
    try:
        with os.fdopen(fd, 'wb') as file:
            out = (b'\xef\xbb\xbf' if raw.startswith(b'\xef\xbb\xbf') else b'') + modified.encode('utf-8')
            file.write(out)
            file.flush()
            os.fsync(file.fileno())
        os.replace(tmp, target)
        check = target.read_text(encoding='utf-8-sig')
        if check.count(NEW_CALLBACK) != 1:
            raise RuntimeError('Installierte Aenderung nicht bestaetigt')
        ast.parse(check, filename=TARGET)
        return 'patched', str(backup)
    except Exception:
        shutil.copy2(backup, target)
        raise
    finally:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass


def main() -> None:
    parser = argparse.ArgumentParser(description='Verknuepft Tagebuch mit lokalem Tagebuch')
    parser.add_argument('jarvis_folder', type=Path)
    a = parser.parse_args()
    status, backup = apply(a.jarvis_folder)
    print('OK: ' + ('Bereits verknuepft' if status == 'already' else 'Tagebuch-Kachel verknuepft'))
    if backup:
        print('Backup: ' + backup)
    print('Noch als signiertes Release veroeffentlichen.')


if __name__ == '__main__':
    main()
