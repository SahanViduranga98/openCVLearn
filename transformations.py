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

#rotation
def rotate(img, angle,rotPoint=None):
    (height, width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    # 1.0 is the scaling factor
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions =(width,height)

    return cv.warpAffine(img,rotMat,dimensions)
# angle --> +-->anti clock wise angle
rotated=rotate(img_resize,45)
cv.imshow('rotated',rotated)

 #flipping an image -->mirrior
 # 0-->mirrir in vertical
 #1-->mirrir in horizontal
 #-1 -->mirrir in both directions
flip=cv.flip(img_resize,0)
cv.imshow('flipped',flip)
cv.waitKey(0)