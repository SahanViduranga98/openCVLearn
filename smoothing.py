#smoothing is done when there is lot of noice in the image due to various factors such as lighting, ...,etc.
# reduce noice by applying bluring tchniques.
#common technique is apply gaussian blur
import cv2 as cv
import numpy as np

img = cv.imread('photos/brownCat.jpg') #read image
cv.imshow('Cat',img) #show image in new window

#Averaging blurring method
average = cv.blur(img,(3,3))#higher the kernal, higher the blur
cv.imshow('Average',average)

#Gaussian Blur Method
gaussian =cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussain',gaussian)

#median blur method
median = cv.medianBlur(img,3)
cv.imshow('Median',median)

#Bilateral Blur
bilateral =cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',bilateral)
cv.waitKey(0)