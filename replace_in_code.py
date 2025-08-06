import re
from pathlib import Path

input_path = Path("/tothepath/file.js")
output_path = Path("/tothepath/outputfile.js")

with input_path.open("r", encoding="utf-8") as file:
    js_code = file.read()

# remove multi-line comments 
js_code = re.sub(r"/\*[\s\S]*?\*/", "", js_code)

# remove single-line comments
js_code = re.sub(r"//.*", "", js_code)

# remove non-ASCII characters
js_code = re.sub(r"[^\x00-\x7F]+", "", js_code)

# split lines, strip whitespace, and remove empty lines
cleaned_lines = [line.strip() for line in js_code.splitlines() if line.strip()]

with output_path.open("w", encoding="utf-8") as file:
    file.write("\n".join(cleaned_lines))

print(f"cleaned code saved to: {output_path.name}")
