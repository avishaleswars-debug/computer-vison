import cv2
import numpy as np
# Load the image
im=cv2.imread('img/im.jpg')
bright=cv2.convertScaleAbs(im,alpha=7.5,beta=50)
blur=cv2.GaussianBlur(im,(3,3),0)
cv2.imshow('Original Image',im)
cv2.imshow('Brightened Image',bright)
cv2.imshow('Blurred Image',blur)
cv2.waitKey(0)