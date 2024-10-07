import cv2 as cv
img = cv.imread('photos/brownCat.jpg') #read image
cv.imshow('Cat',img) #show image in new window

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Simple Threshold
threshold,thresh =cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)
#inverese simple threshold img
threshold,thresh_inv =cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('thresh inv',thresh_inv)

#adaptive threshold
adaptive_thrshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive',adaptive_thrshold)

cv.waitKey(0)