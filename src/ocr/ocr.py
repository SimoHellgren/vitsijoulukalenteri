import re
import numpy as np
import cv2
import pytesseract


def split_screenshot(filepath):
    """Splits Instagram screenshot of the list of responses into individual responses"""
    img = cv2.imread(filepath)

    # crop image
    height, width, channels = img.shape
    left = 200
    right = width - 200
    top = 330

    crop = img[top:, left:right]

    # grayscale, blur and binarize
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = np.where(blur > 200, 0, 255).astype("uint8")

    # dilate
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    dilate = cv2.dilate(thresh, kernel, iterations=4)

    # find contours
    contours = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        part = crop[y : y + h, x : x + w]

        yield part


def extract_vote(data):
    # OCR
    text = pytesseract.image_to_string(data)

    # look for nickname and vote target
    regex = re.compile("(.+)\n[\s\S]+(rosan|simon)")
    match = regex.match(text)

    return match.groups() if match else None