import os
import sys
import types
import unittest
from unittest.mock import patch
import pytest


# Provide a minimal stub for the ``fitz`` module so that ``scripts.data_extraction``
# can be imported without the optional dependency installed.
fitz_stub = types.ModuleType("fitz")
fitz_stub.Page = object
fitz_stub.Rect = object
sys.modules.setdefault("fitz", fitz_stub)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


from scripts.data_extraction import (
    input_test_file_checker,
    pdf_files_path,
    information_extraction_from_pdf,
)


def test_information_extraction_from_pdf():
    with pytest.raises(FileNotFoundError):
        information_extraction_from_pdf("1.pdf")


class TestExtraction(unittest.TestCase):
    def test_input_test_file_checker(self):
        """Ensure missing CLI arguments trigger ``SystemExit``."""
        with patch.object(sys, "argv", ["prog"]):
            with self.assertRaises(SystemExit):
                input_test_file_checker()


def test_pdf_files_path():
    with pytest.raises(FileNotFoundError):
        pdf_files_path("1.pdf")
