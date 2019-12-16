# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         使用Python-OpenCV向图片添加噪声-高斯-椒盐噪声.py
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

def sp_noise(image,prob):
    '''
    添加椒盐噪声
    prob:噪声比例
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def gasuss_noise(image, mean=0.01, var=0.01):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = np.array(image/255, dtype=float)  # 先归一化
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)  # 在恢复成0-255
    #cv.imshow("gasuss", out)
    return out



def show_image(image, win_name=None):
    cv2.imshow(win_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('image.png')
salt = sp_noise(img, 0.01)
gau = gasuss_noise(img)


cv2.imwrite('salt.png', salt)
# show_image(img, 'img')
# show_image(img, 'img')
# show_image(img, 'img')

# 展示所有图像
res = np.hstack((img, salt, gau))
show_image(res)


def main():
    pass


if __name__ == '__main__':
    main()