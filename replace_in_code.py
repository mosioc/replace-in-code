import re
import argparse
from pathlib import Path

def clean_code(file_content, file_extension, remove_comments=True, strip_unicode=True, strip_whitespace=True):
    comment_patterns = {
        '.js': {'single': r'//.*', 'multi': r'/\*[\s\S]*?\*/'},
        '.py': {'single': r'#.*', 'multi': r'"""[\s\S]*?"""|'''[\s\S]*?''''},
        '.html': {'single': None, 'multi': r'<!--[\s\S]*?-->'},
        '.md': {'single': None, 'multi': r'<!--[\s\S]*?-->'}
    }

    patterns = comment_patterns.get(file_extension, {'single': None, 'multi': None})

    # remove multi-line comments
    if remove_comments and patterns['multi']:
        file_content = re.sub(patterns['multi'], '', file_content)

    # remove single-line comments
    if remove_comments and patterns['single']:
        file_content = re.sub(patterns['single'], '', file_content)

    # remove non-ASCII characters
    if strip_unicode:
        file_content = re.sub(r'[^\x00-\x7F]+', '', file_content)

    # split lines, strip whitespace, and remove empty lines
    if strip_whitespace:
        cleaned_lines = [line.strip() for line in file_content.splitlines() if line.strip()]
        file_content = '\n'.join(cleaned_lines)
    else:
        file_content = file_content.strip()

    return file_content

def process_file(input_path, output_path, remove_comments, strip_unicode, strip_whitespace):
    """Process a single file and save the cleaned version."""
    try:
        input_path = Path(input_path)
        output_path = Path(output_path)

        supported_extensions = ['.js', '.py', '.html', '.md']
        if input_path.suffix not in supported_extensions:
            raise ValueError(f"Unsupported file extension: {input_path.suffix}")

        with input_path.open('r', encoding='utf-8') as file:
            content = file.read()

        cleaned_content = clean_code(content, input_path.suffix, remove_comments, strip_unicode, strip_whitespace)

        with output_path.open('w', encoding='utf-8') as file:
            file.write(cleaned_content)

        print(f"Cleaned code saved to: {output_path}")
    except Exception as e:
        print(f"error processing {input_path}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="clean code files by removing comments, non-ASCII characters, and/or whitespace.")
    parser.add_argument("input_files", nargs='+', help="paths to input files (.js, .py, .html, .md)")
    parser.add_argument("--remove-comments", action="store_true", help="remove single-line and multi-line comments")
    parser.add_argument("--strip-unicode", action="store_true", help="remove non-ASCII characters")
    parser.add_argument("--strip-whitespace", action="store_true", help="strip whitespace and remove empty lines")

    args = parser.parse_args()

    if not (args.remove_comments or args.strip_unicode or args.strip_whitespace):
        args.remove_comments = args.strip_unicode = args.strip_whitespace = True

    for input_file in args.input_files:
        input_path = Path(input_file)
        output_file = input_path.with_name(f"{input_path.stem}_cleaned{input_path.suffix}")
        process_file(input_path, output_file, args.remove_comments, args.strip_unicode, args.strip_whitespace)

if __name__ == '__main__':
    main()
