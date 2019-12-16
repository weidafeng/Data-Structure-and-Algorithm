# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         创建简单的进程池pool.py
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

# print(multiprocessing.cpu_count()) # cpu核数 6核

def f(x):
    return x * x


def main():
    pool = multiprocessing.Pool(processes=4) #指定进程数
    result= pool.apply_async(f, (10,)) # 异步非阻塞，不用等待当前进程执行完毕，随时根据系统调度来进行进程切换
    print(result) #<multiprocessing.pool.ApplyResult object at 0x00000242194A3438>
    print(result.get(timeout=1)) # Return the result when it arrives.，超时后报异常

    # 也可以一次传入多个参数、多线程运算
    print(pool.map(f,[i for i in range(10)]))
    # print(pool.map(f, range(10)))  # 两种iterabel数据都行


if __name__ == '__main__':
    main()