"""
1. cv2.bitwise_and(img1, img2) - Performs a bitwise AND operation on two images (Intersection/Common).
2. cv2.bitwise_or(img1, img2) - Performs a bitwise OR operation on two images (Union/Merge).
3. cv2.bitwise_xor(img1, img2) - Performs a bitwise XOR operation on two images.
4. cv2.bitwise_not(img1) - Performs a bitwise NOT operation the image (Colors reversed).

* img1 and img2 should be of same height and width.
** Use only grayscale images or black and white images for bitwise operations.
"""

import cv2
import numpy as np

img1 = np.zeros((400, 400), dtype='uint8')
img2 = np.zeros((400, 400), dtype='uint8')

cv2.circle(img1, (150, 150), 100, 255, -1)
cv2.rectangle(img2, (100, 100), (250, 250), 100, 255, -1)

bitwise_and = cv2.bitwise_and(img2, img1)
bitwise_or = cv2.bitwise_or(img2, img1)
bitwise_not = cv2.bitwise_not(img1)
bitwise_xor = cv2.bitwise_xor(img2, img1)

cv2.imshow('Circle', img1)
cv2.imshow('Rectangle', img2)
cv2.imshow('Bitwise AND', bitwise_and)
cv2.imshow('bitwise OR', bitwise_or)
cv2.imshow('bitwise NOT', bitwise_not)
cv2.imshow('bitwise XOR', bitwise_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()
