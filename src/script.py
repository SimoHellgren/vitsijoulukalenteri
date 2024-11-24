import sys
from ocr.ocr import split_screenshot, extract_vote
import pytesseract

filename = sys.argv[1]

parts = split_screenshot(filename)

for part in parts:
    text = pytesseract.image_to_string(part)
    vote = extract_vote(part)
    print(text)
    print("Result:", vote)
    print("")
    print("*" * 20)
    print()
