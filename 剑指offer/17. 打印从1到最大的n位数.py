#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/23/2020 11:46 AM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        17. 打印从1到最大的n位数
# description:      如最大的3位数，999， 打印从1-999的所有数字
# usage:            


# 本题考查超大整数的存储（python无需考虑，内部用字符串存储大整数）

# 转换思路，全排列每一位都从0到9遍历一次

# 全排列用递归很容易实现——来自剑指offer p117
def Print1toMaxofNDigits2(n):
    if n <= 0:
        return
    num = ['0'] * n
    for i in range(10):  # 0-9
        num[0] = str(i)
        Recursive(num, n, 0)


def Recursive(number, length, index):
    length = len(number)
    if index == length - 1:  # 递归结束的条件：设置好数字的最后一位
        printNumber(number)
        return
    for i in range(10):
        number[index + 1] = str(i)
        Recursive(number, length, index + 1)

# 自定义的打印函数，不打印前面的0
def printNumber(number):
    isbeginning_of_0 = True
    for i in range(len(number)):  # 找到第一个不是0的元素
        if isbeginning_of_0 and number[i] != '0':
            isbeginning_of_0 = False
        if not isbeginning_of_0:
            print(number[i], end="")  # python默认换行，加上end去掉这种默认
    print('\t', end='')


def main():
    Print1toMaxofNDigits2(2)


if __name__ == '__main__':
    main()
