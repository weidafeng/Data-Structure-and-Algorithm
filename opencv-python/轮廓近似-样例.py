# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         轮廓近似-样例.py
# Author:       wdf
# Date:         12/13/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------
import numpy as np
import cv2

# load image and shrink - it's massive
img = cv2.imread('chinese-map.jpg')
# img = cv2.resize(img, None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)

# get a blank canvas for drawing contour on and convert img to grayscale
canvas = np.zeros(img.shape, np.uint8)
img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# filter out small lines between counties
kernel = np.ones((5,5),np.float32)/25
img2gray = cv2.filter2D(img2gray,-1,kernel)
cv2.imshow('img2gray', img2gray)
cv2.waitKey(0)

# threshold the image and extract contours
ret,thresh = cv2.threshold(img2gray,250,255,cv2.THRESH_BINARY_INV)
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


# find the main island (biggest area)
cnt = contours[0]
max_area = cv2.contourArea(cnt)

for cont in contours:
    if cv2.contourArea(cont) > max_area:
        cnt = cont
        max_area = cv2.contourArea(cont)

# define main island contour approx. and hull
perimeter = cv2.arcLength(cnt,True)
epsilon = 0.01*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

hull = cv2.convexHull(cnt)

print(cv2.isContourConvex(cnt))

cv2.drawContours(canvas, cnt, -1, (0, 255, 0), 3)
cv2.drawContours(canvas, [approx], -1, (0, 0, 255), 3)
# cv2.drawContours(canvas, hull, -1, (0, 0, 255), 3) # only displays a few points as well.

cv2.imshow("Contour", canvas)
k = cv2.waitKey(0)

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()


def main():
    pass


if __name__ == '__main__':
    main()