# Rotate image
import cv2

image = cv2.imread('Image Manipulation/image.jpg')

if image is None:
    print("Failed to load image.")
else:
    # Get dimensions of the image
    (h, w) = image.shape[:2]

    # Calculate the center of the image
    center = (w // 2, h // 2)

    # Rotation values
    M = cv2.getRotationMatrix2D(center, 90, 0.5)  # Rotate 45 degrees with a scale of 0.5

    # Perform the rotation
    rotated_image = cv2.warpAffine(image, M, (w, h))

    # Display the original and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated_image)

    # Wait for a key press and close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()



    