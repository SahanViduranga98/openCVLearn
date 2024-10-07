import cv2 as cv
import numpy as np

img = cv.imread('photos/brownCat.jpg') #read image
cv.imshow('Cat',img) #show image in new window

b,g,r = cv.split(img)

blank =np.zeros(img.shape[:2],dtype = 'uint8')

cv.imshow('B',b)
cv.imshow('G',g)
cv.imshow('R',r)


merged= cv.merge([b,g,r])
cv.imshow('Merged_image',merged)


blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

cv.waitKey(0)