import numpy as np
import cv2
while True:
    img = cv2.imread('frame.jpg',0)
    cv2.imshow('image',img)
    k = cv2.waitKey(0)