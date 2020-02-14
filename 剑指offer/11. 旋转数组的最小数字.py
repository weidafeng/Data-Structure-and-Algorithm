#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/22/2020 10:08 AM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        11. 旋转数组的最小数字
# description:      如数组[3,4,5,1,2]是递增数组[1,2,3,4,5]的一个旋转子数组
# usage:            


# 方法一，遍历数组，或使用min()函数，复杂度O(n)
# 没有利用数组有序的特性

# 方法二，二分法, O(logn)
def min_num_in_rotated_array(lst):
    i, j = 0, len(lst) - 1
    while j - i > 1:  # 两个指针相邻的时候终止
        mid = i  # 把mid初始化为i，应对特殊情况：把0个元素移动到后面，即旋转0个元素的情况——一旦发现第一个数字小于最后一个，则说明原数组有序，直接返回第一个元素
        if lst[mid] > lst[i]:  # 说明中间的元素属于第一个递增数组
            i = mid  # 缩小范围
        elif lst[mid] < lst[j]:  # 中间的元素属于第二个递增数组
            j = mid  # 缩小范围
        else:  # 中间的元素与头或尾相等，无法判断他属于第一个还是第二个，只能用顺序查找（在这两个指针范围内）
            return min(lst[i:j])
        mid = (i + j) // 2

    return lst[j]  # 第二个指针指向最小的元素


def main():
    lst = [3, 4, 5, 0, 1, 2, 3]
    lst2 = [1, 0, 1, 1, 1, 1]
    lst3 = [1, 1, 1, 1, 0, 1]
    lst4 = [1, 2, 3, 4]
    print(min_num_in_rotated_array(lst))
    print(min_num_in_rotated_array(lst2))
    print(min_num_in_rotated_array(lst3))
    print(min_num_in_rotated_array(lst4))


if __name__ == '__main__':
    main()
