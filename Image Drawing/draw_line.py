# Draw line on image
import cv2

image = cv2.imread('Image Manipulation/image.jpg')

if image is None:
    print("Failed to load image.")
else:
    pt1 = (50, 50)  # Starting point (x1, y1)
    pt2 = (200, 50)  # Ending point (x2, y2)
    color = (0, 0, 255)  # Green color in BGR
    thickness = 4  # Line thickness

    cv2.line(image, pt1, pt2, color, thickness)

    cv2.imshow('Line on Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()