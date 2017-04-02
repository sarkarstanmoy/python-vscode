#!/usr/bin/env python
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


i = 0
_threshold = 130


def nothing(x):
   global _threshold
   _threshold = x


cap = cv.VideoCapture(0)


while(cap.isOpened()):
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
   
    blur = cv.GaussianBlur(gray, (5, 5), 0)

    #print(_threshold)
    
    ret, thresh1 = cv.threshold(
        blur, 0, 255,  cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    cv.imshow('input', thresh1)
    if(i == 0):
        i = 1
        cv.createTrackbar("Value",
                          "input", 0,
                          255, nothing)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
