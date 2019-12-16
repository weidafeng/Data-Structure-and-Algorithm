# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         进程multiprocessing.py
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

def worker(i):
    name = multiprocessing.current_process().name # 获取当前进程的名字
    print(i, name, " starting")


def main():
    num_list = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,)) # 声明进程
        num_list.append(p)
        p.start()# 开始进程
        p.join() # 阻塞当前进程，直到调用join方法的那个进程执行完，再继续执行当前进程
                # 按顺序执行，要求执行完第一个进程才允许执行第二个 （如果不要求，可以不写）
                # Block the calling thread until the process whose join() method
                 # is called terminates or until the optional timeout occurs.
        print("进程结束")
    print(num_list) # [<Process(Process-1, stopped)>, <Process(Process-2, stopped)>, <Process(Process-3, stopped)>, <Process(Process-4, stopped)>, <Process(Process-5, stopped)>]



if __name__ == '__main__':
    main()