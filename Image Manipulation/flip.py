# Flip image
import cv2

image = cv2.imread('Image Manipulation/image.jpg')

if image is None:
    print("Failed to load image.")
else:
    # Flip the image horizontally
    horizontal_flipped = cv2.flip(image, 1)

    # Flip the image vertically
    vertical_flipped = cv2.flip(image, 0)

    # Flip the image both horizontally and vertically
    both_flipped = cv2.flip(image, -1)

    # Display the original and flipped images
    cv2.imshow('Original Image', image)
    cv2.imshow('Horizontally Flipped Image', horizontal_flipped)
    cv2.imshow('Vertically Flipped Image', vertical_flipped)
    cv2.imshow('Both Flipped Image', both_flipped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()