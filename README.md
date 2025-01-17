# ShortcutCreator

ShortcutCreator is a simple Python program that generates desktop shortcuts for frequently accessed files or URLs on Windows.

## Features

- Create desktop shortcuts for files or URLs.
- Set a custom name for your shortcut.
- Optionally add a description and specify a working directory for the shortcut.

## Requirements

- Python 3.x
- Windows operating system (as it uses Windows-specific libraries)
- `pywin32` and `winshell` packages

## Installation

Before running the program, ensure you have the required packages installed. You can install them using pip:

```bash
pip install pywin32 winshell
```

## Usage

Run the `ShortcutCreator.py` script using Python:

```bash
python ShortcutCreator.py
```

The program will prompt you to enter:

1. The file path or URL for which you want to create a shortcut.
2. The name you wish to give to the shortcut.
3. An optional description for the shortcut.
4. An optional working directory.

After entering the required details, the shortcut will be created on your desktop.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.