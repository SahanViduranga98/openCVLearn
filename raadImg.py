import cv2 as cv
img = cv.imread('photos/brownCat.jpg') #read image
cv.imshow('Cat',img) #show image in new window
cv.waitKey(0)