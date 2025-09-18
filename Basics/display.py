import cv2

# Read an image from file
image = cv2.imread('Basics/image.jpg')

if image is not None:
    print("Image read and displaying successfully.")
    # Display the image
    cv2.imshow('Image', image)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")