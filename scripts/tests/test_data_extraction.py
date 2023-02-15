import pytest
import unittest

from unittest.mock import patch


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
