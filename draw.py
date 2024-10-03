import cv2 as cv
import numpy as np

#create blank image
blank =np.zeros((500,500,3),dtype='uint8')

        #change the color od some spave, [height region,width region] 
blank[0:166,0:250] = 0,0,255


cv.imshow("blank",blank)
cv.waitKey(0)
#img = cv.imread('photos/brownCat.jpg')