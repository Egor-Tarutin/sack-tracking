import os

import cv2
import numpy as np

INPUT_DIR = "data"
OUTPUT_DIR = "masked_data"


poly_coords = []
with open("vercises.txt") as f:
    for i in range(4):
        x1, y1 = f.readline().split()
        x1 = int(x1)
        y1 = int(y1)
        poly_coords.append([x1, y1])
pts = np.array(poly_coords, np.int32)
pts = pts.reshape((-1, 1, 2))

for filename in os.listdir(INPUT_DIR):
    img = cv2.imread(os.path.join(INPUT_DIR, filename))
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, [pts], (255, 255, 255))
    result = cv2.bitwise_and(img, mask)
    cv2.imwrite(os.path.join(OUTPUT_DIR, filename), result)
