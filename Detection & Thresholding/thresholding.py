# Thresholding
import cv2

image = cv2.imread('Detection & Thresholding/image.jpg', cv2.IMREAD_GRAYSCALE)

threshold1 = 60 # Low threshold (Below this value, pixel is set to 0)
threshhold2 = 150 # High threshold (Above this value, pixel is set to 255)

ret, thresh_img = cv2.threshold(image, threshold1, threshhold2, cv2.THRESH_BINARY)

cv2.imshow('Grayscale Image', image)
cv2.imshow('Canny Edge', thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

""""""