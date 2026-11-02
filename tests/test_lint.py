import unittest
from pathlib import Path
from briefkit.lint import lint
from briefkit.cli import main

EX = Path(__file__).resolve().parent.parent / "examples"


class TestLint(unittest.TestCase):
    def test_good(self):
        self.assertTrue(all(ok for ok, _ in lint((EX / "good-brief.md").read_text())))
        self.assertEqual(main([str(EX / "good-brief.md")]), 0)

    def test_bad(self):
        res = lint((EX / "bad-brief.md").read_text())
        self.assertFalse(all(ok for ok, _ in res))
        self.assertEqual(main([str(EX / "bad-brief.md")]), 1)


if __name__ == "__main__":
    unittest.main()
