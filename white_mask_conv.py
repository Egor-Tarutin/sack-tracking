import os

import cv2 as cv

INPUT_DIR = "masked_data"
OUTPUT_DIR = "masks"


for filename in os.listdir(INPUT_DIR):
    img = cv.imread(os.path.join(INPUT_DIR, filename), cv.IMREAD_GRAYSCALE)
    img = cv.medianBlur(img, 5)
    brightness_threshold = 160
    _, th1 = cv.threshold(img, brightness_threshold, 255, cv.THRESH_BINARY)
    cv.imwrite(os.path.join(OUTPUT_DIR, filename), th1)
