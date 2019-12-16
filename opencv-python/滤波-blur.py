# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         滤波-blur.py
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

import cv2
import numpy as np

def show_image(image, win_name):
    cv2.imshow(win_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('salt.png')
show_image(img, 'img')



# 均值blur
blur = cv2.blur(img, ksize=(3,3))

# box filter
box = cv2.boxFilter(img, -1, (3,3),normalize=True) # 与blur函数功能一致
box2 = cv2.boxFilter(img, -1, (3,3),normalize=False) # 不归一化，大于255的都当作255

# gaussian
gau = cv2.GaussianBlur(img, (3,3), sigmaX=0.1) #Gaussian kernel standard deviation in X direction.

# median
median = cv2.medianBlur(img, 3)

results = np.hstack((img, blur, box, box2, gau, median))
print(img.shape, results.shape)

show_image(results, 'result')

def main():
    pass


if __name__ == '__main__':
    main()