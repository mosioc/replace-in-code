import re
from pathlib import Path

def clean_code(file_content, file_extension):
    
    comment_patterns = {
        '.js': {'single': r'//.*', 'multi': r'/\*[\s\S]*?\*/'},
        '.py': {'single': r'#.*', 'multi': r'"""[\s\S]*?"""|'''[\s\S]*?''''},
        '.html': {'single': None, 'multi': r'<!--[\s\S]*?-->'},
        '.md': {'single': None, 'multi': r'<!--[\s\S]*?-->'}
    }

    patterns = comment_patterns.get(file_extension, {'single': None, 'multi': None})

    # remove multi-line comments
    if patterns['multi']:
        file_content = re.sub(patterns['multi'], '', file_content)

    # remove single-line comments
    if patterns['single']:
        file_content = re.sub(patterns['single'], '', file_content)

    # remove non-ASCII characters
    file_content = re.sub(r'[^\x00-\x7F]+', '', file_content)

    # split lines, strip whitespace, and remove empty lines
    cleaned_lines = [line.strip() for line in file_content.splitlines() if line.strip()]

    return '\n'.join(cleaned_lines)

def process_file(input_path, output_path):
    try:
        input_path = Path(input_path)
        output_path = Path(output_path)

        supported_extensions = ['.js', '.py', '.html', '.md']
        if input_path.suffix not in supported_extensions:
            raise ValueError(f"Unsupported file extension: {input_path.suffix}")

        # Read original file content
        with input_path.open('r', encoding='utf-8') as file:
            content = file.read()

        # Clean the content
        cleaned_content = clean_code(content, input_path.suffix)

        # Write cleaned content to output file
        with output_path.open('w', encoding='utf-8') as file:
            file.write(cleaned_content)

        print(f"Cleaned code saved to: {output_path}")
    except Exception as e:
        print(f"error processing {input_path}: {str(e)}")

def main():
    input_files = [
        Path("/topath/jsfile.js"),
        Path("/topath/pyfile.py"),
        Path("/topath/hfile.html"),
        Path("/topath/mdfile.md")
    ]

    for input_file in input_files:
        output_file = input_file.with_name(f"{input_file.stem}_cleaned{input_file.suffix}")
        process_file(input_file, output_file)

if __name__ == '__main__':
    main()
