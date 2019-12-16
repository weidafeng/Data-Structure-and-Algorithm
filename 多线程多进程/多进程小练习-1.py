# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         多进程小练习-1.py
# Author:       wdf
# Date:         12/7/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  生成三个进程，每个进程写一个文件，每个文件中包含进程的名字和当前日期
# Usage：
#-------------------------------------------------------------------------------

import multiprocessing
import time
import os
def worker(path):
    p = multiprocessing.current_process().name
    t = time.asctime()
    with open(path, "w") as f:
        f.write(str(p))
        f.write(str(t))
    print(path, "done.")


def main():
    for i in range(3):
        path = os.path.join(os.getcwd(), str(i)+".txt")
        p = multiprocessing.Process(target=worker, args=(path,))
        p.start()
        p.join()
    print("All done.")


if __name__ == '__main__':
    main()