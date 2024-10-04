#transformation is shifting an image on x/y/z axix

import cv2 as cv
import numpy as np
img = cv.imread('photos/twoCats.jpg')
#cv.imshow('TwoCats', img)
def rescaleFrame(frame,scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions =(width, height)
    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)

img_resize=rescaleFrame(img)
cv.imshow('Cat_resize',img_resize) #show image in new window

#Translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
#-x.-->left
# +x-->right
#-y -->up
# +y --> down

translated =translate(img_resize, 100,100)
cv.imshow('translated',translated)
cv.waitKey(0)