#!/usr/bin/env python3
"""A missing input file must fail cleanly (exit 2), not with a traceback."""

import importlib.util
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "lov-any2pdf" / "scripts" / "md2pdf.py"
SPEC = importlib.util.spec_from_file_location("legacy_any2pdf_md2pdf_input", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class InputValidationTests(unittest.TestCase):
    def test_missing_input_file_exits_2(self):
        argv = ["md2pdf.py", "--input", "does-not-exist.md", "--output", "out.pdf"]
        with patch.object(sys, "argv", argv):
            with self.assertRaises(SystemExit) as ctx:
                MODULE.main()
        self.assertEqual(ctx.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
