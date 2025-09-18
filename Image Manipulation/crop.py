import cv2

# Read an image from file
image = cv2.imread('Image Manipulation/image.jpg')

if image is None:
    print("Failed to load image.")
else:
    cropped_image = image[150:600, 400:800]  # Crop the image (y1:y2, x1:x2)
    cv2.imshow('Original Image', image)
    cv2.imshow('Resized Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()