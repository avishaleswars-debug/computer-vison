import cv2
import numpy as np

# Load the image
image = cv2.imread('img/im.jpg')

gbb = cv2.GaussianBlur(image, (5,5), 0)
mb = cv2.medianBlur(image, 5)
nb = cv2.blur(image, (5,5))

cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Blurred Image', gbb)
cv2.imshow('Median Blurred Image', mb)
cv2.imshow('Average Blurred Image', nb)

cv2.waitKey(0)
cv2.destroyAllWindows()