#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/22/2020 9:25 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        贪婪法
# description:      长度为n的绳子，至少剪一刀，求各段长度乘积最大值
# 示例:
# 长度为8的绳子，3*3*2=18最大

'''
解法一 动态规划法
使用动态规划求解问题的三个特点：
1. 求一个问题的最优解——最大乘积
2. 该问题可以拆成一系列子问题——f(k) * f(n-k)
3. 子问题的最优解就是整体问题的最优解
4. 在分解大问题的过程中，子问题会重复出现，需要重复计算子问题 f(10) = f(4)*f(6), f(4) = f(2) * f(2), f(6) = f(2) * f(3)——f(2)需要重复计算

所以动态规划问题【从上往下分析，从下往上求解】，先计算子问题，再从子问题求解大问题，并存储中间子问题的结果
'''


def max_product_dp(n):
    # 最小的子问题
    if n < 2:  # 最少切一刀，0,1都没法切
        return 0
    if n == 2:  # 1*1
        return 1
    if n == 3:  # 1*2
        return 2

    # 定义数组，存储中间子问题的结果
    cache = [0 for _ in range(n + 1)]
    cache[:4] = [0, 1, 2, 3]  # 长度为i的绳子切成n段后的最大乘积（如 长度为3， 如果不切开（在别的地方切），最大乘积为3）
    max_result = 0
    for i in range(4, n + 1):
        for j in range(1, i // 2 + 1):
            product = cache[j] * cache[i - j]  # 比如长度为8的绳子，切两刀，依次遍历1-7， 2-6， 3-5， 4-4， 其中1、7的最优解已经存储在cache里了
            max_result = max(max_result, product)
        cache[i] = max_result
    
    return cache[-1]


'''
方法二 贪婪法
需要证明为啥每次取最优，能保证整体结果最优

证明方法见p98

长度大于5的绳子，每次取3,且当长度为4的时候，取2-2，而非1-3

'''

def max_product_greedy(n):
    # 最小的子问题
    if n < 2:  # 最少切一刀，0,1都没法切
        return 0
    if n == 2:  # 1*1
        return 1
    if n == 3:  # 1*2
        return 2

    # 尽可能多地取长度为3的子段
    times_of_3 = n // 3

    # 当绳子最后的长度为4时，取2-2，而非1-3， 因为2*2>1*3
    if n - times_of_3 * 3 == 1:
        times_of_3 -= 1

    times_of_2 = (n - times_of_3 * 3) // 2

    return (3 ** times_of_3) * (2 ** times_of_2)

def main():
    print(max_product_dp(8))
    print(max_product_greedy(8))


if __name__ == '__main__':
    main()
