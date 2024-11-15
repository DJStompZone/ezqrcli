# EZQRCLI

The easy QR code command-line interface

## Overview

EZQRCLI is a command-line tool for generating and displaying QR codes in the terminal. It allows you to encode URLs into QR codes and display them with optional text above and below the QR code.

## Installation

To install EZQRCLI, you need to have Python 3.10 or higher. You can install the required dependencies using `pip`:

```sh
pip install ezqrcli
```

## Usage

You can use EZQRCLI from the command line to generate and display QR codes. Below are the available command-line options:

```sh
usage: ezqrcli [-h] [-t TOP_TEXT] [-b BOTTOM_TEXT] [-w CENTER_WEIGHT] url

Generate and display a QR code in the terminal with optional text.

positional arguments:
  url                   The URL to encode in the QR code.

optional arguments:
  -h, --help            show this help message and exit
  -t TOP_TEXT, --top-text TOP_TEXT
                        Text to display above the QR code. Defaults to "Scan this QR code:".
  -b BOTTOM_TEXT, --bottom-text BOTTOM_TEXT
                        Text to display below the QR code. Defaults to the URL, truncated to 50 chars.
  -w CENTER_WEIGHT, --center-weight CENTER_WEIGHT
                        Weight to adjust the centering of the QR code. Default is 1.0.
```

Example usage:

```sh
python -m ezqrcli "https://example.com" -t "Welcome!" -b "Scan to visit example.com"
```

## Code Structure

### `QRCLI` Class

The `QRCLI` class is responsible for generating and displaying QR codes in the terminal. It has the following attributes and methods:

#### Attributes

- `url` (str): The URL to encode in the QR code.
- `top_text` (str): Text to display above the QR code. Default is "Scan this QR code:".
- `bottom_text` (str): Text to display below the QR code. Defaults to the first 50 chars of the URL.
- `center_weight` (float): Weight to adjust the centering of the QR code. Default is 1.0.
- `maxwidth` (int): Maximum width of the QR code.
- `_raw_qr` (str): Raw QR code data.
- `qr_text` (str): Processed QR code text.
- `formatted_qr` (str): Formatted QR code with padding and text.
- `padding` (str): Padding to center the QR code vertically.
- `width` (int): Width of the terminal.
- `height` (int): Height of the terminal.
- `centered_qr_text` (str): Centered QR code text.
- `_raw_lines` (list): List of raw QR code lines.
- `qrcode` (module): QR code module.

#### Methods

- `ensure_qrcode()`: Static method to install the `qrcode` module.
- `_ensure_qrcode()`: Attempts to import the `qrcode` module, installs it if not found.
- `_update()`: Updates the QR code and its attributes.
- `_get_padding() -> str`: Calculates the padding to center the QR code vertically.
- `_get_width() -> int`: Calculates the width of the terminal.
- `_get_height() -> int`: Calculates the height of the terminal.
- `_generate_qr()`: Generates the QR code from the URL.
- `_process_qr()`: Processes the raw QR code to center its lines.
- `_center_qr() -> str`: Centers the QR code text and adds top and bottom text.
- `_format_qr()`: Formats the QR code with padding and text.
- `get_formatted_qr() -> str`: Returns the formatted QR code.
- `get_raw_qr() -> str`: Returns the raw QR code.
- `display_qr()`: Displays the formatted QR code in the terminal.

### `ensure_qrcode` Function

The `ensure_qrcode` function in `ezqrcli/util.py` ensures that the `qrcode` package is installed and available for import. If the module is not found, it installs it using pip.

## Testing

To run the tests, use the following command:

```sh
pytest
```

The tests are located in the `tests` directory and cover various aspects of the `QRCLI` class.

## License

This project is licensed under the MIT License.
