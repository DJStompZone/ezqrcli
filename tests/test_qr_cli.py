# pylint: disable=missing-function-docstring, missing-class-docstring, missing-module-docstring, unused-import, protected-access
import os
import unittest
from unittest.mock import patch
from ezqrcli import QRCLI


class TestQRCLI(unittest.TestCase):

    def setUp(self):
        # Use a patch context manager to mock os.get_terminal_size
        self.terminal_size_patcher = patch(
            "os.get_terminal_size", return_value=os.terminal_size((80, 24))
        )
        self.mock_terminal_size = self.terminal_size_patcher.start()

        # Set up QRCLI instance for tests
        self.url = "https://example.com"
        self.qrcli = QRCLI(self.url)

    def tearDown(self):
        # Stop the patcher after each test
        self.terminal_size_patcher.stop()

    def test_initialization(self):
        self.assertEqual(self.qrcli.url, self.url)
        self.assertEqual(self.qrcli.top_text, "Scan this QR code:")
        self.assertEqual(self.qrcli.bottom_text, self.url)
        self.assertEqual(self.qrcli.center_weight, 1.0)
        self.assertIsNotNone(self.qrcli.qrcode)

    @patch("os.get_terminal_size")
    def test_get_padding(self, mock_terminal_size):
        mock_terminal_size.return_value = os.terminal_size((80, 24))
        expected_padding = "\n" * ((24 - 30) // 2)
        self.assertEqual(self.qrcli._get_padding(), expected_padding)

    @patch("os.get_terminal_size")
    def test_get_width(self, mock_terminal_size):
        mock_terminal_size.return_value = os.terminal_size((80, 24))
        self.assertEqual(self.qrcli._get_width(), 80)

    @patch("os.get_terminal_size")
    def test_get_height(self, mock_terminal_size):
        mock_terminal_size.return_value = os.terminal_size((80, 24))
        self.assertEqual(self.qrcli._get_height(), 24 - 30)

    @patch("qrcode.QRCode.print_ascii")
    def test_generate_qr(self, mock_print_ascii):
        # Set the mock to write "QR_CODE" into the provided StringIO buffer
        def mock_print_ascii_function(out):
            out.write("QR_CODE")

        mock_print_ascii.side_effect = mock_print_ascii_function
        self.qrcli._generate_qr()
        self.assertEqual(self.qrcli._raw_qr.strip(), "QR_CODE")

    def test_process_qr(self):
        # pylint: disable=line-too-long
        self.qrcli._raw_lines = ["line1", "line2"]
        self.qrcli._process_qr()
        expected_text = "              line1               \n              line2               "  # match centered text
        self.assertEqual(self.qrcli.qr_text, expected_text)

    @patch("os.get_terminal_size")
    def test_center_qr(self, mock_terminal_size):
        mock_terminal_size.return_value = os.terminal_size((80, 24))
        self.qrcli.qr_text = "line1\nline2"
        centered_qr = self.qrcli._center_qr()
        self.assertIn("Scan this QR code:", centered_qr)
        self.assertIn("line1", centered_qr)
        self.assertIn("line2", centered_qr)
        self.assertIn(self.url, centered_qr)

    def test_format_qr(self):
        self.qrcli._format_qr()
        self.assertIn("Scan this QR code:", self.qrcli.formatted_qr)
        self.assertIn(self.url, self.qrcli.formatted_qr)

    @patch("builtins.print")
    def test_display_qr(self, mock_print):
        self.qrcli.display_qr()
        mock_print.assert_called_with(self.qrcli.formatted_qr)


if __name__ == "__main__":
    unittest.main()
