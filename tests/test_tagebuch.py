# Tests fuer die Tagebuch-Kachel. Lokal: python -m unittest discover -s tests -v
import ast
from pathlib import Path
import tempfile
import unittest

from tools.patch_tagebuch import NEW_CALLBACK, patch_text, apply


class TagebuchPatchTests(unittest.TestCase):
    def test_callback(self):
        original = "tiles = [('Tagebuch', lambda:_launch(self,'Tagebuch'))]\n"
        patched, status = patch_text(original)
        self.assertEqual(status, 'patched')
        self.assertIn("http://127.0.0.1:18767/", patched)
        self.assertEqual(patched.count(NEW_CALLBACK), 1)
        ast.parse(patched)
        again, status = patch_text(patched)
        self.assertEqual(status, 'already')
        self.assertEqual(again, patched)

    def test_unknown_code_rejected(self):
        with self.assertRaises(ValueError):
            patch_text("tiles = []\n")
        with self.assertRaises(ValueError):
            patch_text("x=lambda:_launch(self,'Tagebuch')\ny=lambda:_launch(self,'Tagebuch')\n")

    def test_backup_and_repeated_install(self):
        raw = b"tiles = [('Tagebuch', lambda:_launch(self,'Tagebuch'))]\n"
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root/'jarvis.py').write_text('# fixture', encoding='utf-8')
            target = root/'jarvis_modern_ui.py'
            target.write_bytes(raw)
            status, backup = apply(root)
            self.assertEqual(status, 'patched')
            self.assertEqual(Path(backup).read_bytes(), raw)
            self.assertIn(NEW_CALLBACK, target.read_text('utf-8'))
            status, backup = apply(root)
            self.assertEqual((status, backup), ('already', None))


if __name__ == '__main__':
    unittest.main()
