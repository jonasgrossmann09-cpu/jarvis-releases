import json
import stat
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools.inspect_release import inspect_release_archive, read_public_manifest_summary, safe_name


class StructuralInspectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.zip = Path(self.temp.name) / "sample.zip"

    def archive(self, files):
        with zipfile.ZipFile(self.zip, "w") as z:
            for name, data in files:
                z.writestr(name, data, compress_type=zipfile.ZIP_DEFLATED)
        return self.zip

    def test_valid_archive(self):
        report = inspect_release_archive(self.archive([("jarvis.py", "print('ok')")]))
        self.assertEqual(report["entry_count"], 1)
        self.assertFalse(report["signature_checked"])

    def test_traversal(self):
        with self.assertRaises(ValueError):
            inspect_release_archive(self.archive([("../bad.py", "bad")]))

    def test_windows_path(self):
        self.assertFalse(safe_name("C:/Windows/bad.exe"))
        self.assertFalse(safe_name("../a.py"))
        self.assertFalse(safe_name("dir\\file.py"))

    def test_reserved_names(self):
        self.assertFalse(safe_name("aux.txt"))
        self.assertFalse(safe_name("bin/COM1"))
        self.assertFalse(safe_name("file. "))

    def test_case_collision(self):
        with self.assertRaises(ValueError):
            inspect_release_archive(self.archive([("file.py", "a"), ("FILE.PY", "b")]))

    def test_extra_directory(self):
        with self.assertRaises(ValueError):
            inspect_release_archive(self.archive([("foo/", "")]))

    def test_symlink(self):
        info = zipfile.ZipInfo("link")
        info.create_system = 3
        info.external_attr = (stat.S_IFLNK | 0o777) << 16
        with zipfile.ZipFile(self.zip, "w") as z:
            z.writestr(info, "target")
        with self.assertRaises(ValueError):
            inspect_release_archive(self.zip)

    def test_bad_json(self):
        path = Path(self.temp.name) / "manifest.json"
        path.write_text("not json")
        with self.assertRaises(json.JSONDecodeError):
            read_public_manifest_summary(path)

    def test_manifest_does_not_leak_secrets(self):
        path = Path(self.temp.name) / "manifest.json"
        path.write_text(json.dumps({"version": "2.2.4", "token": "sensitive", "signature": "hidden"}))
        report = read_public_manifest_summary(path)
        self.assertIn("token", report["top_level_fields"])
        self.assertNotIn("sensitive", str(report))
        self.assertNotIn("hidden", str(report))
        self.assertFalse(report["signature_checked"])

    def test_excessive_compression_ratio(self):
        with self.assertRaises(ValueError):
            inspect_release_archive(self.archive([("huge.txt", "A" * 180_000)]))


if __name__ == "__main__":
    unittest.main()
