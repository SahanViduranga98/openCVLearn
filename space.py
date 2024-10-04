import cv2 as cv

img = cv.imread('photos/brownCat.jpg') #read image
cv.imshow('Cat',img) #show image in new window
#BGR to gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Cat_gray',gray) #show image in new window

#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('Cat_HSV',hsv) #show image in new window

#BGR to gray
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('Cat_lab',lab) #show image in new window

cv.waitKey(0)