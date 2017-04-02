
import numpy as py
import cv2 as cv

im = cv.imread("Lena.png")
imgray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
ret, thresh1 = cv.threshold(
        imgray, 0, 255,  cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
_,contours, hierarchy = cv.findContours(thresh1,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
img = cv.drawContours(im,contours,-1,(0,0,0),-1)
cv.imshow("value",img)


cv.waitKey(0)
cv.destroyAllWindows()
