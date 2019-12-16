# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         2的整数幂.py
# Author:       wdf
# Date:         11/28/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  判断一个整数是不是2的整数幂
# Usage：
#-------------------------------------------------------------------------------

# 方法一，从1开始，每次乘以2，如果两数相等，则是；
# 如果该数大于n，则不是
# O(log(n))
def is_power_of_two(n):
    tmp = 1
    while tmp <= n :
        if n == tmp:
            return True

        tmp = 2 * tmp
    return False


# 方法二，用移位优化乘法
# O(log(n))
def is_power_of_two_2(n):
    tmp = 1
    while tmp <= n:
        if n == tmp:
            return True

        tmp = tmp<<1 # 左移一位，相当于乘以2
    return False

# 方法三
# O(1)
# 转化为2进制， 利用二进制与位运算的特性
'''
把2的整数次幂转换成二进制数， 会有什么样的共同点？
2   10
4   100
8   1000
16  10000

减一？
2-1     01
4-1     011
8-1     0111
16-1    01111

# 与运算？n&(n-1)
2&（2-1）     0
4&（4-1）     0
8&（8-1）     0

'''

def is_power_of_two_3(n):
    return not n & (n-1)

def main():
    print(is_power_of_two(16))
    print(is_power_of_two_2(16))
    print(is_power_of_two_3(16))

    print(is_power_of_two(161))
    print(is_power_of_two_2(161))
    print(is_power_of_two_3(161))


if __name__ == '__main__':
    main()