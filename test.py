from ocr.image import split_screenshot, extract_vote
import pytesseract

parts = split_screenshot("test.jpg")

for part in parts:
    text = pytesseract.image_to_string(part)
    vote = extract_vote(part)
    print(text)
    print("Result:", vote)
    print("")
    print("*" * 20)
    print()
