# Draw circle on image
import cv2

image = cv2.imread('Image Manipulation/image.jpg')

if image is None:
    print("Failed to load image.")
else:
    center = (600, 400)  # Circle center (x, y)
    radius = 150  # Circle radius
    color = (0, 0, 255)  # Red color in BGR
    thickness = 4  # Line thickness (-1 for filled circle)

    cv2.circle(image, center, radius, color, thickness)

    cv2.imshow('Circle on Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()