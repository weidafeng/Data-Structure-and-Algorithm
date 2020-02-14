#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/22/2020 10:22 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        15-3. 一个整数需要修改几位可以变成另一个整数
# description:      如整数10的二进制位为1010， 13的二进制位为1101，则需要修改3位
# usage:            


# 异或——两个数不一样的地方为1
# 计算异或结果中有多少个1

def times_of_change(m,n):
    # 异或
    xor = m ^ n

    # 统计 1 的个数
    count = 0
    while xor:
        count += 1
        xor = xor & (xor - 1)
    return count


def main():
    print(times_of_change(10, 13))


if __name__ == '__main__':
    main()
