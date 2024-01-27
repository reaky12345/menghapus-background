import cv2
import cv2
import numpy as np

def remove_background(input_path, output_path):
    image = cv2.imread(input_path)
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([0, 40, 40])
    upper_bound = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imwrite(output_path, result)

input_image_path = "logo.jpeg"
output_image_path = "logo.png"

remove_background(input_image_path, output_image_path)