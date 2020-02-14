#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/21/2020 1:40 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        10. 斐波那契数列
# description:      
# usage:            


def fibonacci(n):
    # 方法一，单纯的递归
    if n <= 0:
        return 0
    if n==1:
        return 1 
    return fibonacci(n-1) + fibonacci(n-2)


# 递归效率太低，需要大量的重复计算
# 考虑把中间结果存储起来，可以极大地提高效率
def fibonacci_2(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    n_minus_1, n_minus_2 = 0, 1
    
    for i in range(n):
        n_minus_1, n_minus_2 = n_minus_1 + n_minus_2, n_minus_1
    return n_minus_1


def main():
    n = 8
    print(fibonacci(n))
    print(fibonacci_2(n))
    import timeit
    print(timeit.timeit('fibonacci(10)', globals=globals()))
    print(timeit.timeit('fibonacci_2(10)', globals=globals()))
    '''
    21
    21
    17.196012099999997
    0.6414350999999989
    '''

if __name__ == '__main__':
    main()
