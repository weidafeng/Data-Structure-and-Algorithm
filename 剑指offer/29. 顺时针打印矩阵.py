#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/7/2020 2:52 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        29. 顺时针打印矩阵
# description:      从（0,0）开始，顺时针打印矩阵
# usage:            

# 这道题没有技巧，关键是细心、考虑循环的边界条件

# 第一步，实现打印一圈的函数
def print_circle(lst, start):
    '''
    从起始点开始，顺时针遍历一圈
    :param lst:  二维矩阵 
    :param start:  起始坐标（start，start）
    :return: 
    '''
    end_x = len(lst) - start
    end_y = len(lst[start]) - start

    # 从左到右打印一行（上面的行）
    for i in range(start, end_x):
        print(lst[start][i], end=' ')
    print()

    # 打印一圈，不一定需要四步，可能只需要3步、或者2步、甚至1步

    # 从上到下打印一列（右边的列）
    if start < end_y:  # 还有列元素未遍历
        for j in range(start + 1, end_y):
            print(lst[j][end_x-1], end=' ')
        print()

    # 从右到左打印一行（下面的行）
    if start < end_x and start < end_y:
        for i in range(end_x - 1 - 1, start - 1, -1):
            print(lst[end_y-1][i], end=' ')
        print()

    # 从下到上打印一列（左边的列）
    if start < end_x and start + 1 < end_y:
        for j in range(end_y - 1 - 1, start, -1):
            print(lst[j][start], end=' ')
        print()
    print('*'*10)

# 第二步， 遍历，得到每个起点、顺时针遍历（注意边界条件）
def clockwise_print(lst):
    if len(lst) == 0 or len(lst[0]) == 0:
        return 
    start = 0  # 从（0,0）开始
    
    # 每次取左上角（start，start）作为开始遍历的起点
    while len(lst) > start * 2 and len(lst[0]) > start * 2:  
        # 循环继续的条件：
        # col > 2*start and row > 2*start
        print_circle(lst, start)
        start += 1
    
    print('done')

def main():
    lst = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print_circle(lst, 0)
    print_circle(lst, 1)
    clockwise_print(lst)

if __name__ == '__main__':
    main()
