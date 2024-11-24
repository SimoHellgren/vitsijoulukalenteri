from pathlib import Path
import json
from ocr.ocr import split_screenshot, extract_vote

result = {}

for file in Path("/images").glob("**/*.*"):
    parts = split_screenshot(file)

    votes = map(extract_vote, parts)

    result[str(file)] = {name: vote for name, vote in votes}


with open("/output/output.json", "w") as f:
    json.dump(result, f, indent=2)
