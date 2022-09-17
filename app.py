import ocr
import cv2

if __name__ == "__main__":
    img = cv2.imread('imgs/textimg.png')
    cv2.imshow("input", img)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    ocr.get_text_coord_pairs(img_rgb)