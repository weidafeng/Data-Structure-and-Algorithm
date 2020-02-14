#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/6/2020 8:42 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        21. 调整数组顺序使奇数位于偶数前面
# description:      调整数组顺序，使奇数位于数组前面，偶数位于后面
# usage:            

# 双指针
def reorder_1(lst):
    i, j = 0, len(lst) - 1
    while i <= j:
        while i < j and lst[i] % 2:  # 左边是奇数，往右移
            i += 1
        while i < j and lst[j] % 2 == 0:  # 右边是偶数，往左移
            j -= 1

        # 交换奇数和偶数
        lst[i], lst[j] = lst[j], lst[i]
        # 交换后不要忘了减小范围
        i += 1
        j -= 1
        print(i, j, lst)
    return lst


def main():
    lst = list(range(10))
    print(reorder_1(lst))

    lst = [int(i) for i in list('111122233314')]
    print(reorder_1(lst))


if __name__ == '__main__':
    main()
