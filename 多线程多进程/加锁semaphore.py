# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         加锁semaphore.py
# Author:       wdf
# Date:         12/8/2019
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

def worker(sem, i):
    sem.acquire() # 获得锁
    print(multiprocessing.current_process().name + " 被获取")
    time.sleep(1)
    sem.release() # 释放锁
    print(multiprocessing.current_process().name + " 被释放")

def main():
    # 设置限制，最多三个进程同时访问共享资源
    sem = multiprocessing.Semaphore(value=3)  # 同时加3个锁
    for i in range(6): # 创建6个进程
        p = multiprocessing.Process(target=worker, args=(sem, i))
        p.start()


if __name__ == '__main__':
    main()