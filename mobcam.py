import urllib.request
import cv2
import numpy as np
import imutils
url='http://192.168.131.90:8080/shot.jpg'
while True:
    imgPath=urllib.request.urlopen(url)
    imgNP=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgNP,-1)
    frame=imutils.resize(frame,width=450)
    cv2.imshow("Frame",frame)
    if ord('q')==cv2.waitKey(10):
           exit(0)
