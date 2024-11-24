from ocr.image import split_screenshot
from PIL import Image
import pytesseract

parts = split_screenshot("test.jpg")

for part in parts:
    text = pytesseract.image_to_string(part)
    print(text)
    print("")
    print("*" * 20)
    print()
