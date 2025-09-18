# Load image
# Grayscale conversion
# Display dimensions
# Display grayscale image
# Save grayscale image

import cv2

image_location = input("Enter the path to the image file: ")

image = cv2.imread(image_location)

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Image converted to grayscale successfully.")

    show_save = input("Do you want to display or save the grayscale image? (1 for display, 2 for save): ")

    if show_save == "1":
        cv2.imshow('Grayscale Image', gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif show_save == "2":
        save_location = input("Enter the path to save the grayscale image: ")
        success = cv2.imwrite(save_location, gray)
        if success:
            print("Image saved successfully.")
        else:
            print("Error: Could not save the image.")
    else:
        print("Invalid choice.")
else:
    print("Error: Could not read the image.")

