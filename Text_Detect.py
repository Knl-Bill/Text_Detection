import cv2
import numpy as np
from PIL import Image
from pytesseract import image_to_string

def get_string(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite(src_path + "removed_noise.png", img)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.imwrite(src_path + "thres.png", img)
    result = image_to_string(Image.open(src_path + "thres.png"))
    return result
if __file__ == '__main__':
    src_path = r'D:\python\captchatext.png'
    print('--- Start recognize text from image ---')
    print(get_string(src_path) )
    print("------ Done -------")