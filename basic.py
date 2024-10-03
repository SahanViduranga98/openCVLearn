import cv2 as cv

img = cv.imread('photos/brownCat.jpg') #read image
cv.imshow('Cat',img) #show image in new window
# gray scale image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Cat_gary',gray) #show image in new window

#blur an image
#(7,7) is the kernel size, has to an odd number, increasing kernal number-->more blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur) #show image in new window
cv.waitKey(0)