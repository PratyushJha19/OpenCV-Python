# Canny Egde Detection
import cv2

image = cv2.imread('Detection & Thresholding/image.jpg', cv2.IMREAD_GRAYSCALE)

# Threshold same is used as in thresholding
edges = cv2.Canny(image, 50, 150)

cv2.imshow('Grayscale Image', image)
cv2.imshow('Canny Edge', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()