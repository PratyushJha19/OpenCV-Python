import cv2

img = cv2.imread('Shape Detection/rectangle.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)


# Find Contours (Gets the outlines or boundaries of the shapes)
contours, heirarchy = cv2.findContours(thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

# RETR_EXTERNAL - Only external contours
# RETR_LIST - All contours (No heirarchy)
# RETR_TREE - All contours (With heirarchy)

# Draw Contours
cv2.drawContours(img, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=2)

# Shape Detection
for contour in contours:
    approx = cv2.approxPolyDP(curve = contour, epsilon = 0.01 * cv2.arcLength(contour, True), closed = True)
    corners  = len(approx)

    if corners == 3:
        shape_name = "Triangle"
    elif corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners > 5:
        shape_name = "Circle"
    else:
        shape_name = "Unknown"

    cv2.drawContours(img, [approx], 0, (0, 0, 255), 4)
    x = approx.ravel()[0]
    y = approx.ravel()[1] -10
    cv2.putText(img, shape_name, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255))

cv2.imshow('Contour', img)
cv2.waitKey(0)
cv2.destroyAllWindows()