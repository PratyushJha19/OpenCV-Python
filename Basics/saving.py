import cv2

# Read an image from file
image = cv2.imread('Basics/image.jpg')

if image is not None:
    success = cv2.imwrite('Basics/output_image.jpg', image)
    if success:
        print("Image saved successfully.")
    else:
        print("Error: Could not save the image.")
else:
    print("Error: Could not read the image.")