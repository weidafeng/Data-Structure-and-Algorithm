#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/22/2020 10:19 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        15-2. 判断一个数是不是2的n次方
# description:      
# usage:            

# 2 的n次方，二进制形式只有一个1，其他位都是0
# 去掉最后一个1，如果结果是0，说明是2的n次方
def is_pow_of_2(n):
    return not n & (n - 1)

def main():
    print(is_pow_of_2(2))
    print(is_pow_of_2(4))
    print(is_pow_of_2(10))


if __name__ == '__main__':
    main()
