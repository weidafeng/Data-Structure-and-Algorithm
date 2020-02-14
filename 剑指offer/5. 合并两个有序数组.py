#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/20/2020 10:43 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        5. 合并两个有序数组
# description:      两个有序数组，合并到同一个，保证合并后的数组有序
# usage:            


def merge_two_sorted_array(lst1, lst2):
    '''
    两个有序数组，合并到lst1， 保证结果有序

    # 方法一，类似第五题（字符串替换空格）的思想，从后往前

    :param lst1:
    :param lst2:
    :return:
    '''
    i, j = len(lst1) - 1, len(lst2) - 1
    lst1 += lst2  # 先给lst1 开辟足够的空间
    while i >= 0 and j >= 0:
        if lst1[i] > lst2[j]:
            lst1[i + j + 1] = lst1[i]
            i -= 1
        else:
            lst1[i + j + 1] = lst2[j]
            j -= 1
    if j > 0:  # 遍历完一个数组后，第二个数组还有剩余（一定是最小的几个元素），直接赋值
        lst1[:j] = lst2[:j]
    # 另一种情况，第一个数组还有剩余，不需要操作，因为一定是最小的元素，本身就有序
    return lst1


def main():
    lst1 = [-1, 1, 2, 3, 6]
    lst2 = [-1, 0, 2, 3, 5, 7, 8, 9]
    res = lst1 + lst2
    print(sorted(res))
    print(merge_two_sorted_array(lst1,lst2))


if __name__ == '__main__':
    main()
