import cv2 as cv
img = cv.imread('photos/brownCat.jpg')

def rescaleFrame(frame,scale=1.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions =(width, height)
    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)

img = cv.imread('photos/brownCat.jpg') #read image
cv.imshow('Cat',img) #show image in new window
img_resize=rescaleFrame(img)
cv.imshow('Cat_resize',img_resize) #show image in new window
cv.waitKey(0)