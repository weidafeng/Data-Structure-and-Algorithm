#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/23/2020 11:10 AM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        16. 整数的m次幂
# description:      实现pow(n, m)
# usage:            


# 方法一，m个n相乘
def power(n, m):
    # 特殊情况
    if n == 0:  # 0 的任何次幂都没有意义，这里指定为0
        return 0
    if m == 0:
        return 1
    if m == 1:
        return n

    # 考虑负数
    flag = False
    res = 1
    if m < 0:
        m = -m
        flag = True
    while m:
        res *= n
        m -= 1
    return 1 / res if flag else res


# 方法二，上面要乘m次，可以考虑减少运算次数
# 比如求16次方，可以求8次方 的平方

def power_2(n, m):
    # 特殊情况
    if n == 0:  # 0 的任何次幂都没有意义，这里指定为0
        return 0
    if m == 0:
        return 1
    if m == 1:
        return n

    flag = False
    res = n
    if m < 0:
        flag = True
        m = -m
        while m > 1:  # m是偶数、且不为0
            res = res * res
            m //= 2
    if flag:
        return 1 / (res * n) if m else 1 / res  # 如果最后还有m没用完，说明m是个奇数，还有1个没乘
    else:
        return res * n if m else res  # 如果最后还有m没用完，说明m是个奇数，还有1个没乘


# 递归实现
def power_2_recursive(n, m):
    if m > 0:
        return _helper_power_2_recursive(n, m)
    else:
        return 1 / _helper_power_2_recursive(n, -m)


def _helper_power_2_recursive(n, m):
    # 特殊情况
    if n == 0:  # 0 的任何次幂都没有意义，这里指定为0
        return 0
    if m == 0:
        return 1
    if m == 1:
        return n

    res = _helper_power_2_recursive(n, m // 2)
    res *= res

    if m % 2:  # 奇数（只有最深一层可能用到一次）
        res *= n
    return res


# 使用位运算，进一步优化
def power_3_recursive(n, m):
    if m > 0:
        return _helper_power_3_recursive(n, m)
    else:
        return 1 / _helper_power_3_recursive(n, -m)


def _helper_power_3_recursive(n, m):
    # 特殊情况
    if n == 0:  # 0 的任何次幂都没有意义，这里指定为0
        return 0
    if m == 0:
        return 1
    if m == 1:
        return n

    res = _helper_power_3_recursive(n, m >> 1)  # 位运算
    res *= res

    if m & 1:  # 奇数（只有最深一层可能用到一次）  # 位运算
        res *= n
    return res


def main():
    print(power(2, 5))
    print(power_2(2, -3))
    print(power_2_recursive(2, -3))


if __name__ == '__main__':
    main()
