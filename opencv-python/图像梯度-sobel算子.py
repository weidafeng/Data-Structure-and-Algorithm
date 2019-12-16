# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         图像梯度-sobel算子.py
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


img = cv2.imread('image.png',flags=cv2.IMREAD_GRAYSCALE) # 灰度
show_image(img, 'gray')

# sobel x (左边 - 右边） 求水平方向梯度
sobel_x = cv2.Sobel(img,ddepth= -1, # 保留图像深度不变
                    dx=1,  # 计算水平方向梯度
                    dy=0,  # 不计算竖直方向梯度
                    ksize=3, # sobel的kernel size
                    scale=cv2.CV_64F # 扩大像素值的保存范围，因为左边-右边，可能会有负数值，这里保留负数信息
                    )
show_image(sobel_x, 'sobel_x')
# 因为图像像素值只能是0-255， sobel_x显示时，把负数过滤掉了，统一设置为0
# 需显式显示负数值
sobel_x_total = cv2.convertScaleAbs(sobel_x)
show_image(sobel_x_total, 'sobel_x_total')

result = np.hstack((sobel_x, sobel_x_total))
show_image(result, 'result')


# sobel y （下边 - 上边） 求竖直方向梯度
sobel_y = cv2.Sobel(img, -1,
                    dx=0,
                    dy=1,
                    ksize=3,
                    scale=cv2.CV_64F)
sobel_y_all = cv2.convertScaleAbs(sobel_y)
show_image(sobel_y_all, 'sobel_y_all')

# 把水平方向和竖直方向的梯度加到一起
# (sobel_y_all * 0.5 +  sobel_x_total * 0.5)
sobel_xy = cv2.addWeighted(sobel_y_all, 0.5, sobel_x_total, 0.5, 0)
show_image(sobel_xy, 'sobel_xy')


# 不建议同时对水平方向和竖直方向求梯度，会导致重影和间断
sobel_x_and_y_sim = cv2.Sobel(img, -1,
                    dx=1, # x
                    dy=1, # y
                    ksize=3,
                    scale=cv2.CV_64F)
show_image(sobel_x_and_y_sim, 'sobel_x_and_y_sim')
result = np.hstack((sobel_xy, sobel_x_and_y_sim))
show_image(result, 'result2')





def main():
    pass


if __name__ == '__main__':
    main()