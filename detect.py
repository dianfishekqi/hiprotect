#!/usr/bin/python
import numpy as np
import cv2
import datetime
import time
camera = cv2.VideoCapture(0)
camera.set(3,1920)
camera.set(4,1080)

while True:
    if(camera.isOpened()):
	retVal , image = camera.read()
	timeofCap = str(datetime.datetime.now())
        if retVal:
            cv2.imwrite("captures/capture-"+timeofCap+".jpg",image)
	    print "Image Captured"	
        time.sleep(2)
    else:
        camera = camera.open(0)
        camera.set(3,1920)
        camera.set(4,1080)



