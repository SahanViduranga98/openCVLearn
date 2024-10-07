#histgram gives a high level intution of the pixel distribution in the image 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('photos/brownCat.jpg') #read image
cv.imshow('Cat',img) #show image in new window
blank = np.zeros(img.shape[:2],dtype='uint8')

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray_hist =cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('Gray Scale Histogram')
plt.plot(gray_hist)
plt.xlabel('Bins')
plt.ylabel('density')
plt.slim([0,256])
plt.show()
cv.waitKey(0)