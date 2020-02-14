#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/12/2020 1:59 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        42. 连续子数组的最大和
# description:      给定一个数组，有整数也有负数， 求所有子数组的和的最大值      
# usage:            
# lst = [1, -2, 3, 10, -4, 7, 2, -5]
# res = 18
# explain: [3, 10, -4, 7, 2]


# # 用动态规划的思路，先写出表达式
#         --- f(i-1) + lst[i]  if i != 0 and f(i-1) > 0
#         |
# f(i) =  |
#         |
#         --- lst[i]           if i == 0 or f(i-1) <= 0

def find_great_sub_array(lst):
    cur_sum = 0
    great_sum = 0
    for i in range(len(lst)):
        if i == 0 or cur_sum <= 0:
            cur_sum = lst[i]
        else:
            cur_sum += lst[i]

        if cur_sum > great_sum:
            great_sum = cur_sum

    return great_sum


def main():
    lst = [1, -2, 3, 10, -4, 7, 2, -5]
    print(find_great_sub_array(lst))


if __name__ == '__main__':
    main()
