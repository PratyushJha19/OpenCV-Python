# Write text on image
import cv2

image = cv2.imread('Image Manipulation/image.jpg')

if image is None:
    print("Failed to load image.")
else:
    text = "Writing text on image..."  # Text to write
    origin = (50, 500)  # Starting point (x, y)
    color = (0, 0, 0)  # Red color in BGR
    font = cv2.FONT_HERSHEY_SIMPLEX  # Font type
    font_scale = 1  # Font scale
    thickness = 4  # Line thickness (-1 for filled circle)

    cv2.putText(image, text, origin, font, font_scale, color, thickness)

    cv2.imshow('Write Text on Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()