import sys
from pathlib import Path
import json
import pytesseract
from ocr import split_screenshot


GLOB_PATTERN = sys.argv[1]

result = {}

for file in Path("/images").glob(GLOB_PATTERN):
    parts = split_screenshot(file)

    voters = [pytesseract.image_to_string(part).strip("\n") for part in parts]

    result[str(file)] = voters


with open("/output/output.json", "w") as f:
    json.dump(result, f, indent=2)
