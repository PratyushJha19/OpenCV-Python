import cv2

# Read an image from file
image = cv2.imread('Basics/image.jpg')

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Image converted to grayscale successfully.")
    cv2.imshow('Grayscale Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")