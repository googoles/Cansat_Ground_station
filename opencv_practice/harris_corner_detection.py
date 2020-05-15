import cv2
import numpy as np

image = cv2.imread('line.jpg')
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
img_gray = np.float32(img_gray)

dst = cv2.cornerHarris(img_gray, 2, 3, 0.04)

image[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', image)
cv2.waitKey(0)