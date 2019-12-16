# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         主线程.py
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

import threading
import time


# 在主线程中启动其他线程
def worker(i):
    print("new thread %s"%i)
    t = threading.current_thread() # 当前线程
    time.sleep(10) # 设置线程休眠
    print(t.getName())
'''
课程地址：https://www.bilibili.com/video/av54045374/

一般（单线程情况）我们可能会认为程序是线性进行，先运行完new_t，之后再运行后面的t

但我们的new_t是新启动的线程——多线程，所以程序不会等前面执行完之后再执行后面的，
而是同时执行（看起来是同时）

为了验证，可以在new_t.start()和t上打两个断点，
单线程情况下，程序必须在new_t执行完之后才会调到下一个断点（设置了10s的休眠）

但这是多线程情况，会 **立即** 跳转到下一个断点
'''
new_t =  threading.Thread(target=worker,args={10}, name='new thread') # 通过线程对象Thread（）创建一个新的线程
new_t.start() # 启动

'''
如果不使用多线程，必须等待worker(10）执行完才会跳转到下一条
'''
worker(10)

# 默认是在主线程
t = threading.current_thread()
print(t.getName()) # MainThread


def main():
    pass


if __name__ == '__main__':
    main()