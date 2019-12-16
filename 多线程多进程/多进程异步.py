# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         多进程异步.py
# Author:       wdf
# Date:         12/9/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------


# 测试multipleprocessing
from multiprocessing import pool


def worker(num):
    for i in range(num):
        print(i, end=' ')
    return('num = ', num)  # 需要有返回值


if __name__ == "__main__":
    mypool = pool.Pool(processes=3)
    results = []
    for num in range(10):
        mypool.apply_async(func=worker, args=(num, ), callback=results.append)
    mypool.close()
    mypool.join()
    print(results)
