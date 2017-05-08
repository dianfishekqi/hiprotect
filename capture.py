#!/usr/bin/python
import numpy as np
import cv2
import datetime
import time
import sys

#Delay between captures
delay = 30

if len(sys.argv) != 1:
    delay = sys.argv[1]

camera = cv2.VideoCapture()

while True:
    if cv2.VideoCapture().isOpened():
        try:
	        retVal , image = camera.read()
        except:
            print "Error while grabing the frame"
            pass
	    timeofCap = str(datetime.datetime.now())
        if retVal:
            try:
                cv2.imwrite("captures/capture-"+timeofCap+".jpg",image)
                print "Image Captured"
            except:
                print "Error occured while trying to save the image"
                pass
        time.sleep(2)
    else:
        try:
            camera = camera.open(0)
            camera.set(CV_CAP_PROP_FRAME_WIDTH,1920)
            camera.set(CV_CAP_PROP_FRAME_HEIGHT,1080)
        except:
            pass


'''
Camera.set Attributes:
    CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
    CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
    CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
    CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
    CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
    CV_CAP_PROP_FPS Frame rate.
    CV_CAP_PROP_FOURCC 4-character code of codec.
    CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
    CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
    CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
    CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
    CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
    CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
    CV_CAP_PROP_HUE Hue of the image (only for cameras).
    CV_CAP_PROP_GAIN Gain of the image (only for cameras).
    CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
    CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
    CV_CAP_PROP_WHITE_BALANCE_U The U value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
    CV_CAP_PROP_WHITE_BALANCE_V The V value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
    CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
    CV_CAP_PROP_ISO_SPEED The ISO speed of the camera (note: only supported by DC1394 v 2.x backend currently)
    CV_CAP_PROP_BUFFERSIZE Amount of frames stored in internal buffer memory (note: only supported by DC1394 v 2.x backend currently)
'''
