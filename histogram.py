#histgram gives a high level intution of the pixel distribution in the image 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('photos/brownCat.jpg') #read image
cv.imshow('Cat',img) #show image in new window
blank = np.zeros(img.shape[:2],dtype='uint8')
#mask has to be in same size as img
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)

masked =cv.bitwise_and(gray,gray,mask=mask)

gray_hist =cv.calcHist([gray],[0],masked,[256],[0,256])

plt.figure()
plt.title('Gray Scale Histogram')
plt.plot(gray_hist)
plt.xlabel('Bins')
plt.ylabel('density')
plt.xlim([0,256])


#creating histogram for a color image
masked_color =cv.bitwise_and(img,img,mask=mask)
colors =('b','g','r')
plt.figure()
plt.title('Color Histogram')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)