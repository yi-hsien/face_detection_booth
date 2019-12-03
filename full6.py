import numpy as np
import cv2
import os
import subprocess
import time

os.chdir("/home/pi/opencv-3.0.0/data/haarcascades")

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
n = 0
video = None

while 1:
    if n > 1:
        for i in xrange(16):
            cap.grab()
    ret, img = cap.read()
    if not ret :
        n = 0
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#this line is only for testing
        if w > 100 and h > 100:
            video = True
    n += 1
    k = cv2.waitKey(1000) & 0xff
    if k == 27:
        break
    if video:
        os.system( "omxplayer -b /home/pi/vid.mp4")#depends on the name of the video
        time.sleep(1.5)#put how many seconds in here
        video = None
        
cap.release()
cv2.destroyAllWindows()
