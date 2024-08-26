import cv2 as cv

img=cv.imread("book.jpg")
img=cv.cvtColor(img,cv.COLOR_RGB2GRAY)

_,result=cv.threshold(img,50,255,cv.THRESH_BINARY)

adaptive=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,13,9)


cv.imshow("Adaptive",adaptive)

cv.waitKey(0)
cv.destroyAllWindows()