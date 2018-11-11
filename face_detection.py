import numpy as np
import cv2
print (dir(cv2))
print(dir(cv2.imread))
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('C:/Anaconda3/envs/python2/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Anaconda3/envs/python2/Lib/site-packages/cv2/data/haarcascade_eye.xml')
img = cv2.imread('asd.jpg')
print (img.shape) # 959L, 959 W, 3l
print (img.size)# number of pixel 959 x959 x 3 = 2759043
print (img.dtype)  # unit 8 image data type
print(959*959*3)
print(cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(gray)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)


for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()