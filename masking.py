import cv2 as cv
import numpy as np
img = cv.imread('photos/brownCat.jpg') #read image
cv.imshow('Cat',img) #show image in new window
blank = np.zeros(img.shape[:2],dtype='uint8')

#mask has to be in same size as img
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Mask',mask)

masked =cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image',masked)



cv.waitKey(0)