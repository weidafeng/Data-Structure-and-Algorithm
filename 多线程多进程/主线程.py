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

# 默认是在主线程
t = threading.current_thread()
print(t.getName()) # MainThread


# 在主线程中启动其他线程
def worker(i):
    print("new thread %s"%i)
    t = threading.current_thread() # 当前线程
    print(t.getName())

new_t =  threading.Thread(target=worker,args={10}, name='new thread') # 通过线程对象Thread（）创建一个新的线程
'''参数意义：
        target： 执行的目标函数名
        args： 目标函数所需要的参数列表
        name: 线程名（如不指定，默认为Thread-1）
'''

# 上面只是定义了一个线程，需要启动
new_t.start() # 启动


def main():
    pass


if __name__ == '__main__':
    main()