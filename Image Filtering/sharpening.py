import cv2
import numpy as np

image = cv2.imread('Image Filtering/image.jpg')

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)

cv2.imshow("original", image)
cv2.imshow("Sharpened", sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()