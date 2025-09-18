import cv2

# Read an image from file
image = cv2.imread('Basics/image.jpg')

if image is not None:
    h, w, c = image.shape
    print(f"Height: {h}, Width: {w}, Channels: {c}")
else:
    print("Error: Could not read the image.")