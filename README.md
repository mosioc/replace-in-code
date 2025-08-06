# Replace-in-Code
Replace or remove unwanted strings in code files using customizable regex patterns

## Features
- Removes multi-line comments (`/* ... */`)
- Removes single-line comments (`// ...`)
- Removes non-ASCII characters
- Strips whitespace and removes empty lines
- Preserves core JavaScript code structure

## Prerequisites
- Python 3.x
- Standard libraries: `re`, `pathlib`

## Usage
1. Place the script in the same directory as the input JavaScript file or specify the correct file paths.
2. Update the `input_path` and `output_path` variables in the script to point to your input and desired output files.
3. Run the script using:
   ```bash
   python script_name.py
   ```
4. The cleaned JavaScript code will be saved to the specified output file.

## Input and Output
- **Input**: A JavaScript file (e.g., `file.js`)
- **Output**: A cleaned JavaScript file (e.g., `outputfile.js`)

## Notes
- Ensure the input file exists and is readable.
- The script overwrites the output file if it already exists.
- The script assumes UTF-8 encoding for both input and output files.

## Limitations
- Non-ASCII characters are removed, which may affect code with intentional non-ASCII content.
- Complex comment structures or edge cases may require additional handling.
