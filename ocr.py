import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('imgs/textimg.png')
cv2.imshow("input", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

d = pytesseract.image_to_string(img_rgb)
print(d)