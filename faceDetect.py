import cv2 as cv
img = cv.imread('photos/group.jpg') #read image
cv.imshow('Cat',img) #show image in new window


gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY) #gray
cv.imshow('gray',gray) #show image in new window

haar_cascade = cv.CascadeClassifier('haar_face.xml') #class

faces_rect =haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)
print(f'Number of faces={len(faces_rect)} faces)')


for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('deteted faces',img)
cv.waitKey(0)