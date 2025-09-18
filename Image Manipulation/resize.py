import cv2

# Read an image from file
image = cv2.imread('Image Manipulation/image.jpg')

if image is None:
    print("Failed to load image.")
else:
    # Resize the image to 300x300 (width x height) pixels
    resized_image = cv2.resize(image, (300, 300))

    # Display the original and resized images
    cv2.imshow('Original Image', image)
    cv2.imshow('Resized Image', resized_image)

    # Wait for a key press and close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('Image Manipulation/resized_image.jpg', resized_image)