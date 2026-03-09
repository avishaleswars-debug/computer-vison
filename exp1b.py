import cv2
import numpy as np
img=cv2.imread('img/im.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)