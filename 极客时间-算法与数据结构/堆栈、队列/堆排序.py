# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         堆排序.py
# Author:       wdf
# Date:         11/24/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  使用python内置标准库实现堆排序
# Usage：
#-------------------------------------------------------------------------------

# 默认是最小堆
from heapq import heappush, heappop, heapify

def heap_sort(lst):
    h = []
    for val in lst:
        heappush(h, val)
    return [heappop(h) for _ in range(len(h))]


def main():
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    res = heap_sort(lst)
    print(lst)
    print(res)

    heapify(lst)
    print(lst)

if __name__ == '__main__':
    main()