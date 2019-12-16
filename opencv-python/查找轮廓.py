# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         查找轮廓.py
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
import random
import cv2

def show_image(image, win_name=None):
    cv2.imshow(win_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 1. 读取图像、转化成灰度
img = cv2.imread('counter.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# 灰度

# 2. 二值化处理
# 大于阈值127的都置为255， 小于127的置为0
'''
这个函数有四个参数，第一个原图像，第二个进行分类的阈值，第三个是高于（低于）阈值时赋予的新值，第四个是一个方法选择参数，常用的有： 
• cv2.THRESH_BINARY（黑白二值） 
• cv2.THRESH_BINARY_INV（黑白二值反转） 
• cv2.THRESH_TRUNC （得到的图像为多像素值） 
• cv2.THRESH_TOZERO 
• cv2.THRESH_TOZERO_INV 
该函数有两个返回值，第一个retVal（得到的阈值值（在后面一个方法中会用到）），第二个就是阈值化后的图像。 
'''
ret, thresh = cv2.threshold(gray,thresh=127, maxval=255, type=cv2.THRESH_BINARY )
print(type(ret), ret)  #  阈值
print(type(thresh), thresh.shape)
show_image(np.hstack((gray, thresh)), 'thresh')

# 3. find counter
'''
cv2.findContours()

三个输入参数：输入图像（二值图像），轮廓检索方式，轮廓近似方法

1.轮廓检索方式
cv2.RETR_EXTERNAL	只检测外轮廓
cv2.RETR_LIST	检测的轮廓不建立等级关系
cv2.RETR_CCOMP	建立两个等级的轮廓，上面一层为外边界，里面一层为内孔的边界信息
cv2.RETR_TREE	建立一个等级树结构的轮廓

2.轮廓近似办法
cv2.CHAIN_APPROX_NONE	存储所有边界点
cv2.CHAIN_APPROX_SIMPLE	压缩垂直、水平、对角方向，只保留端点
cv2.CHAIN_APPROX_TX89_L1	使用teh-Chini近似算法
cv2.CHAIN_APPROX_TC89_KCOS	使用teh-Chini近似算法
 
2个返回值：轮廓，轮廓的层析结构
'''
contours, hierarchy = cv2.findContours(thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
print(type(contours), np.array(contours).shape)
print(type(hierarchy), hierarchy)
# print(type(hierarchy), hierarchy)

# 4.绘制轮廓
draw_img = cv2.drawContours(img,
                            contours,
                            contourIdx= -1, # -1表示绘制所有轮廓， 其他值指定单个轮廓索引
                            color=(0,0,255),
                            thickness=2)
show_image(draw_img, 'thresh')

# 5. 使用轮廓特征计算信息
# 面积
print(cv2.contourArea(contours[1]))
# 周长
print(cv2.arcLength(contours[1], closed=True))

# 6. 轮廓近似， 用尽可能少的线近似轮廓
epsilon = 0.1 * cv2.arcLength(contours[1], closed=True) # 根据周长设置阈值
approx_contour = cv2.approxPolyDP(gray, epsilon, closed=True)  # 轮廓近似

draw_img = img.copy()
res = cv2.drawContours(img, [approx_contour], -1, (0,255,0), 2)
show_image(res, "res")



def main():
    pass


if __name__ == '__main__':
    main()