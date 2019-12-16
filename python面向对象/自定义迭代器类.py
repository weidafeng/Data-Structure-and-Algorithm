# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         自定义迭代器类.py
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

'''自定义迭代器类，需要实现最基本的两个方法：
1. __iter__()，
2. __next__()
'''

class MyIter(object):
    def __init__(self,lst):
        self.idx = 0
        self.lst = lst
        self.length = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.length:
            val = self.lst[self.idx]
            self.idx += 1
            return val
        else: # 越界，引发异常
            raise StopIteration()


def main():
    my_lst = MyIter(range(3))
    print(next(my_lst))
    print(next(my_lst))
    print(next(my_lst))
    print(next(my_lst)) # 异常


if __name__ == '__main__':
    main()