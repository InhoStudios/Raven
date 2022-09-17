import ocr
import cv2

def mouse_coords(event, x, y, flags, param):
    global mouseX, mouseY 
    if event == cv2.EVENT_LBUTTONDBLCLK:
        mouseX, mouseY = x, y

if __name__ == "__main__":
    img = cv2.imread('imgs/skew.jpeg')
    deskewed = ocr.deskew(img)
    cv2.imshow("title", deskewed)
    cv2.waitKey(0)
    # cap = cv2.VideoCapture(0)
    # cv2.setMouseCallback('Input', mouse_coords)

    # if (not cap.isOpened()):
    #     raise IOError("Cannot open webcam")

    # while True:
    #     ret, frame = cap.read()
    #     frame = cv2.resize(frame, None, fx=0.5, fy=0.5,interpolation=cv2.INTER_AREA)
    #     cv2.imshow('Input', frame)

    #     c = cv2.waitKey(1)
    #     if c == 27:
    #         break
    #     print(ocr.get_word_by_coords(mouseX, mouseY, frame))

    # cap.release()
    # cv2.destroyAllWindows()