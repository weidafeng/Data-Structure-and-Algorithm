# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         加锁lock.py
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

'''
进程加锁是为了确保数据的一致性，比如读写锁，多个进程操作同一个文件，
但如果一个进程读取、但还没来得及写入的时候，另外的进程也读取了该文件，会导致错误。

因此需要加锁，来保证同意时刻只有一个进程可以执行某几行代码
'''

# 示例
import multiprocessing
import time

def my_lock(lock, name):
    lock.acquire() # 获得锁  # 在获得锁和释放锁之间，写自己的代码
    print("获得锁，", name)
    lock.release() # 释放锁
    print("释放锁，", name)



def main():
    lock = multiprocessing.Lock() # 创建一个共享锁实例
    t_start = time.time()
    for num in range(20):
        p = multiprocessing.Process(target=my_lock, args=(lock, num)) # 创建线程
        p.start()
        p.join() #进程阻塞
    t_end_1 = time.time()

    print(t_start - t_end_1)
    for num in range(20):
        p = multiprocessing.Process(target=my_lock, args=(lock, num))  # 创建线程
        p.start()
        # p.join()  # 不阻塞
    t_end_2 = time.time()
    print(t_end_2 - t_end_1)  # 明显快很多——没有等for循环执行完毕，就执行了后面的程序


if __name__ == '__main__':
    main()