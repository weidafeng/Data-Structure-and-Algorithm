# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         多进程的模板程序.py
# Author:       wdf
# Date:         12/7/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

import multiprocessing
import time
import requests

# 创建两个一样的函数
# 打印网站的前20个字符
def func1(url):
    time.sleep(3)
    response = requests.get(url)
    result = response.text
    print("func-1: ", result[:20])

# 打印网站的后20个字符
def func2(url):
    time.sleep(3)
    response = requests.get(url)
    result = response.text
    print("func-2: ", result[-20:])


def main():
    p1 = multiprocessing.Process(target=func1, args=("https://www.baidu.com",))
    p2 = multiprocessing.Process(target=func2, args=("https://www.bilibili.com",))

    p1.start()
    p2.start()

    p1.join()  # 阻塞当前进程，直到调用join方法的p1进程执行完毕
    p2.join()

    print("All done.")

if __name__ == '__main__':
    main()