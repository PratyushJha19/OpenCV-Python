import cv2

image = cv2.imread("Basics/image.jpg")

if image is None:
    print("Error: Could not read the image.")
else:
    print("Image read successfully.")