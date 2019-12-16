# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         bisect库.py
# Author:       wdf
# Date:         12/16/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------


# 使用bisect示例
import bisect
import random

random.seed(1)

print('New Pos Contents')
print('--- --- --------')

l = []
for i in range(1, 15):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)  # 找到合适的位置（默认是bisec_left)
    bisect.insort(l, r)  # 结果数组l， 待插入数字r， 每次按照从小到大的顺序，找到合适的位置插入
    print('%3d %3d' % (r, position), l)
'''
New Pos Contents
--- --- --------
 18   0 [18]
 73   1 [18, 73]
 98   2 [18, 73, 98]
  9   0 [9, 18, 73, 98]
 33   2 [9, 18, 33, 73, 98]
 16   1 [9, 16, 18, 33, 73, 98]
 64   4 [9, 16, 18, 33, 64, 73, 98]
 98   7 [9, 16, 18, 33, 64, 73, 98, 98]
 58   4 [9, 16, 18, 33, 58, 64, 73, 98, 98]
 61   5 [9, 16, 18, 33, 58, 61, 64, 73, 98, 98]
 84   8 [9, 16, 18, 33, 58, 61, 64, 73, 84, 98, 98]
 49   4 [9, 16, 18, 33, 49, 58, 61, 64, 73, 84, 98, 98]
 27   3 [9, 16, 18, 27, 33, 49, 58, 61, 64, 73, 84, 98, 98]
 13   1 [9, 13, 16, 18, 27, 33, 49, 58, 61, 64, 73, 84, 98, 98]
 '''

# 另一个典型应用，计算分数等级：
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)  # 找到合适的位置，但不进行真正的插入
    return grades[i]

print([grade(score)for score in [33, 99, 77, 70, 89, 90, 100]])
'''['F', 'A', 'C', 'C', 'B', 'A', 'A']'''


### 实现二分查找
def binary_search_bisect(lst, x):
    from bisect import bisect_left
    i = bisect_left(lst, x)
    if i != len(lst) and lst[i] == x:  # 后面这个判断主要是为了保证 输入数组为有序
        return i
    return None
lst = [33, 99, 77, 70, 89, 90, 100]
lst.sort() # 输入的一定要是有序数组
print(lst)
print(binary_search_bisect(lst, 70))

