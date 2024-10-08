import cv2 as cv
import numpy as np
img = cv.imread('photos/brownCat.jpg') #read image
cv.imshow('Cat',img) #show image in new window


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Laplacion method
lap=cv.Laplacian(gray,cv.CV_64F )
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacion',lap) #show Laplacion


#Sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow('SobelX',sobelx) #show
cv.imshow('SobelY',sobely) #show
cv.imshow('Combined',combined_sobel)
cv.waitKey(0)