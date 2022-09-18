import cv2
import pytesseract
from pytesseract import Output
import numpy as np
import math

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def get_text_coord_pairs(opencvimg):
    d = pytesseract.image_to_data(opencvimg, output_type=Output.DICT)
    n_tokens = len(d['text'])
    word_coords = []
    for i in range(n_tokens):
        if (int(d['conf'][i] > 60)):
            word = {'x': d['left'][i], 'y': d['top'][i], 'w': d['width'][i], 'h': d['height'][i], 'txt': d['text'][i]}
            if (word['txt'] != ""):
                word_coords.append(word)
    return word_coords

def get_word_by_coords(x, y, img, size=250):
    if math.isnan(x) or math.isnan(y):
        return ""
    img_crop = get_grayscale(img[int(y):int(y+size), int(x):int(x+size)])
    return pytesseract.image_to_string(img)

# preprocessing functions from nanonets.com
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.diilate(image, kernel, iterations=1)

def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations=1)

def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

def canny(image):
    return cv2.Canny(image, 100, 200)

def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)