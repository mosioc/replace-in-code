# Replace-in-Code
Replace or remove unwanted strings in code files using customizable regex patterns

## Features
- Supports multiple file types: JavaScript (.js), Python (.py), HTML (.html), Markdown (.md)
- Configurable cleaning presets:
  - `--remove-comments`: Removes single-line and multi-line comments
  - `--strip-unicode`: Removes non-ASCII characters
  - `--strip-whitespace`: Strips whitespace and removes empty lines
- Preserves core code or content structure
- Processes multiple files via command-line arguments

## Prerequisites
- Python 3.x
- Standard libraries: `re`, `pathlib`, `argparse`

## Installation
1. Save the script as `code_cleaner.py`.
2. Ensure Python 3.x is installed on your system.

## Usage
Run the script from the command line, specifying input files and optional cleaning presets:

```bash
python code_cleaner.py /path/to/file1.js /path/to/file2.py --remove-comments --strip-unicode --strip-whitespace
```

### Command-Line Arguments
- `input_files`: One or more paths to input files (.js, .py, .html, .md)
- `--remove-comments`: Remove single-line and multi-line comments (optional)
- `--strip-unicode`: Remove non-ASCII characters (optional)
- `--strip-whitespace`: Strip whitespace and remove empty lines (optional)

### Example
To clean a JavaScript and Python file, removing only comments:
```bash
python code_cleaner.py /path/to/jsfile.js /path/to/pyfile.py --remove-comments
```

## Supported File Types and Comment Patterns
- **JavaScript (.js)**: Removes `//` single-line and `/* */` multi-line comments
- **Python (.py)**: Removes `#` single-line and `""" """` or `''' '''` multi-line comments
- **HTML (.html)**: Removes `<!-- -->` multi-line comments
- **Markdown (.md)**: Removes `<!-- -->` multi-line comments

## Notes
- Ensure input files exist and are readable.
- The script overwrites output files if they already exist.
- The script assumes UTF-8 encoding for both input and output files.
- At least one cleaning option must be implicitly or explicitly enabled.

## Limitations
- Complex comment structures or edge cases may require additional handling.
- The script processes files sequentially; large files may impact performance.
