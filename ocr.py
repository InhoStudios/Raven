import cv2
import pytesseract
from pytesseract import Output

def get_text_coord_pairs(opencvimg):
    d = pytesseract.image_to_data(opencvimg, output_type=Output.DICT)
    n_tokens = len(d['text'])
    for i in range(n_tokens):
        if int(d['conf'][i] > 60):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            opencvimg = cv2.rectangle(opencvimg, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', opencvimg)
    cv2.waitKey(0)