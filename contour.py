import cv2 as cv
import numpy as np
img = cv.imread('photos/brownCat.jpg')
cv.imshow('brown cat', img)

#gray image
gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('brown cat_gray', gray)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('black',blank)
#edge detection
canny = cv.Canny(img,125,175)
cv.imshow('brown cat_edge detection', canny)



ret,thresh =cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('brown cat_thresh', thresh)

#contour detection
#contours is a list of all the coordinates of the contours that were fouund in the image
#hierarchy is a list of hierachical representations of the contours
#cv.RETR_LIST returns the all the contours find in the image
#cv.RETR_Exterior returns the all the contours found in the  outside
#cv.RETR_Tree returns the all the contours found in the interior
#cv.CHAIN_APPROX_NONE,v.CHAIN_APPROX_SIMPLE

contours,hirerarchies =cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)
cv.waitKey(0)