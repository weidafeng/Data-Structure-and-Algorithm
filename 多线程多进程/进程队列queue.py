# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         进程队列queue.py
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

'''使用多进程，一个进程放10个数，另一个进程取这10个数'''

import multiprocessing

def put_data(queue):
    # 入队列
    for i in range(10):
        queue.put("number: "+str(i))
        print("放入数据：", i)

def get_data(queue):
    # 出队列
    for i in range(10):
        result = queue.get()
        print(result)

def main():
    # 创建一个队列实例（主进程）
    queue = multiprocessing.Queue()

    # 创建两个子进程实例 p1，p2， 调用队列queue
    p1 = multiprocessing.Process(target=put_data, args=(queue,))
    p2 = multiprocessing.Process(target=get_data, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("队列是否为空：", queue.empty())

if __name__ == '__main__':
    main()