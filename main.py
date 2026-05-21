import cv2
import numpy as np

# Load image
image = cv2.imread("image.jpg")

# Convert image to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Red color range
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# Blue color range
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

# Green color range
lower_green = np.array([40, 40, 40])
upper_green = np.array([70, 255, 255])

# Create masks
red_mask = cv2.inRange(hsv, lower_red, upper_red)
blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
green_mask = cv2.inRange(hsv, lower_green, upper_green)

# Show results
cv2.imshow("Original Image", image)
cv2.imshow("Red Color Detection", red_mask)
cv2.imshow("Blue Color Detection", blue_mask)
cv2.imshow("Green Color Detection", green_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()