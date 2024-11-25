import numpy as np
import cv2


def crop(filepath):
    img = cv2.imread(filepath)

    # crop image
    height, width, channels = img.shape

    # crop width by percentage to accomodate different image sizes
    left = int(width * 0.2)
    right = int(width * 0.7)

    # heuristic for different image sizes
    top = int(400 * width / 1080)

    crop = img[top:, left:right]

    return crop


def split_screenshot(filepath):
    """Splits Instagram screenshot of the list of responses into individual responses"""

    cropped = crop(filepath)

    # only keep things that are "black enough" -
    # this corresponds to usernames
    lower = np.array([0, 0, 0])  # "black"
    upper = np.array([100, 100, 100])  # "gray"
    mask = cv2.inRange(cropped, lower, upper)

    # dilate to form contiguous ranges
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilate = cv2.dilate(mask, kernel, iterations=5)

    # find contours
    contours = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    for i, c in enumerate(contours, 1):
        x, y, w, h = cv2.boundingRect(c)

        # use aspect ratio as a filter to weed out silly data
        if w / float(h) > 2:
            yield mask[y : y + h, x : x + w]
