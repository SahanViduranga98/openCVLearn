import cv2 as cv
import numpy as np

#create blank image
blank =np.zeros((500,500,3),dtype='uint8')

        #change the color od some region, [height region,width region] 
#blank[0:166,0:250] = 0,0,255
#draw a rectangle in an image
#(image, start point, height & width, color of rectangle, thickness)
cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=2)
cv.imshow("blank",blank)
cv.waitKey(0)
#img = cv.imread('photos/brownCat.jpg')