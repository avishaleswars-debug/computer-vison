import cv2
import numpy as np

img = cv2.imread('img/im.jpg',0)

eq = cv2.equalizeHist(img)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
cv2.imshow("Input Image", img)
cv2.imshow("Equalized Image", eq)
eqhist=cv2.calcHist([eq],[0],None,[256],[0,256])
cv2.imshow("Input Image Histogram", hist)
cv2.imshow("Equalized Image Histogram", eqhist)
cv2.waitKey(0)
cv2.destroyAllWindows()
