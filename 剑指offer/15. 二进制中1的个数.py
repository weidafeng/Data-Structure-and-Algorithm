#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/22/2020 10:03 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        15. 二进制中1的个数
# description:      
# usage:            

# n & (n - 1) 去掉最后一个1

def count_1(n):
    count = 0
    while n:
        count += 1
        n = n & (n - 1)
    return count



def main():
    print(count_1(3))


if __name__ == '__main__':
    main()
