import os
import sys
import json
import types
import pytest
import unittest

from unittest.mock import patch


# Allow importing modules from the scripts directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Provide a minimal stub for the ``fitz`` package used in ``data_extraction``.
fitz_stub = types.ModuleType("fitz")
fitz_stub.open = lambda *args, **kwargs: None
fitz_stub.Rect = object
fitz_stub.Page = object
sys.modules.setdefault("fitz", fitz_stub)

from data_extraction import (
    input_test_file_checker,
    pdf_files_path,
    information_extraction_from_pdf,
)


def test_information_extraction_from_pdf():
    with pytest.raises(FileNotFoundError):
        information_extraction_from_pdf("1.pdf")


class TestExtraction(unittest.TestCase):
    def test_input_test_file_checker(self):
        with self.assertRaises(Exception):
            # arrange
            path = "anything.pdf"
            # act
            with patch("project.sys.exit") as exit_mock:
                path = input_test_file_checker(path)
                # assert
                exit_mock.assert_called_once_with("Too many command-line arguments")


def test_pdf_files_path():
    with pytest.raises(FileNotFoundError):
        pdf_files_path("1.pdf")


def test_data_file_overwrite(monkeypatch, tmp_path):
    """Ensure data.json contains a single JSON array after multiple runs."""
    # change working directory to a temporary path so data.json is created there
    monkeypatch.chdir(tmp_path)

    # Ensure no pdf files are processed
    with patch("data_extraction.pdf_files_path", return_value=[]):
        # First execution creates the file
        information_extraction_from_pdf("dummy")
        with open("data.json", "r") as f:
            content_first = f.read()

    # Run again and check that file is overwritten, not appended
    with patch("data_extraction.pdf_files_path", return_value=[]):
        information_extraction_from_pdf("dummy")
        with open("data.json", "r") as f:
            content_second = f.read()

    assert content_first == content_second
    # Content should be a valid JSON array
    assert json.loads(content_second) == []
