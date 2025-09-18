import cv2

image = cv2.imread('Image Filtering/image.jpg')

blurred_image = cv2.GaussianBlur(image, (21, 21), 6)

cv2.imshow("original", image)
cv2.imshow("blurred", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()