import os,sys,PIL
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

import cv2
def main():
    # Sample Image for Testing
    #imagepath = "Sample/1.jpg"
    imagepath = raw_input("enter image path")

    savepath = "Sample/2.jpg"

    #Accept other imputs
    #pivot=["0.0","0.0"]
    pivot=raw_input("Enter centre point for zooming X,Y").split(",")
    pivot[0]=float(pivot[0])
    pivot[1]=float(pivot[1])


    #scale=1.5
    scale=float(raw_input("Enter zoom value>1"))


    image = cv2.imread(imagepath,1)


    height,width,z = image.shape
    x,y,_=image.shape

    x=x/(scale*2)
    y=y/(scale*2)
    xmin=0;ymin=0;xmax=width;ymax=height

    #pivot[0]=width/2
    #pivot[1]=height/2

    tempx1=pivot[0]-x
    tempx2=pivot[0]+x
    tempy1 = pivot[1] - y
    tempy2 = pivot[1] + y

    if tempx1<=0:
        xmin=0
    else:
        xmin=tempx1
    if tempx2>=width:
        xmax=width
    else:
        xmax=tempx2

    if tempy1<=0:
        ymin=0
    else:
        ymin=tempy1
    if tempy2>=height:
        ymax=height
    else:
        ymax=tempy2


    cropped = image[int(xmin):int(xmax),int(ymin):int(ymax)]



    cv2.imwrite(savepath,cropped)
if __name__ == '__main__':
    main()