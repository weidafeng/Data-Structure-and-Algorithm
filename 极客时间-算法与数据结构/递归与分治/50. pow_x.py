# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         50. pow_x.py
# Author:       wdf
# Date:         11/18/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

# 计算x 的n 次方
# pow(x, n)

# method 1. 调用库函数
# Runtime: 36 ms, faster than 55.74% of Python3 online submissions for Pow(x, n).
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Pow(x, n).
def pow_x(x, n):
    return pow(x, n)


# 暴力循环，逐个相乘 （超时）
# Time Limit Exceeded

# Last executed input
# 0.00001
# 2147483647
def pow_x_1(x, n):
    result = 1
    if n >= 0:
        for i in range(n):
            result *= x
    else:
        for i in range(abs(n)):
            result /= x
    return result


# 递归、分治法
# n -> n/2 -> n/4 ... -> 1
def pow_x_2(x, n):
    if not n : # 终止条件
        return 1
    if n < 0:
        return 1 / pow_x_2(x, -n)

    if n % 2 : # n is odd number
        return x * pow_x_2(x, n-1)

    return pow_x_2(x*x, n // 2)

# 自己写递归
def pow_x_3(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x

    if n < 0:
        return 1 / pow_x_3(x, -n)

    if n % 2 : # 奇数
        return x * pow_x_3(x, n-1)
    else: # 偶数
        return pow_x_3(x*x, n //2)


# 非递归实现 + 位运算（老师认为最好的代码）
# Runtime: 28 ms, faster than 88.85% of Python3 online submissions for Pow(x, n).
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Pow(x, n).
# TODO 再理解
def pow_x_4(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    pow = 1 # 表示当前的x的值
    while n:
        if n & 1: # 奇数
            pow *= x  # 只在奇数情况下计算结果（一定会用到，比如n=2， n//2 = 1)
        x *= x # 不管对于奇数、偶数
        n >>= 1 # n 每次除以 2
    return pow


# 常规非递归
# Runtime: 24 ms, faster than 95.90% of Python3 online submissions for Pow(x, n).
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Pow(x, n).
def pow_x_5(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    while n > 0:
        if n % 2 == 0:  # 偶数， x*=x,奇数不变
            x *= x
            n //= 2
        result *= x
        n -= 1  # n 每次 减少 1（与上面位运算方法对比）
    return result


def main():
    print(pow_x(2, -2))
    print(pow_x_1(2, -2))
    print(pow_x_3(2, 10))
    print(pow_x_2(2, 10))
    print(pow_x_3(2, -2))
    print(pow_x_2(2, -2))

    print(pow_x_4(2, 11))
    print(pow_x_5(2, 11))
    # print(pow_x_4(2, -2))


if __name__ == '__main__':
    main()