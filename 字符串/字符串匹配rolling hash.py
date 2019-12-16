# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         字符串匹配rolling hash.py
# Author:       wdf
# Date:         12/14/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------
'''
Rabin-Karp算法的思想：

1.假设待匹配字符串的长度为M，目标字符串的长度为N（N>M）；
2.首先计算待匹配字符串的hash值，计算目标字符串前M个字符的hash值；
3.比较前面计算的两个hash值，比较次数N-M+1：
    1.若hash值不相等，则继续计算目标字符串的下一个长度为M的字符子串的hash值
    2.若hash值相同，则需要使用朴素算法再次判断是否为相同的字串；


https://blog.csdn.net/yanghua_kobe/article/details/8914970
'''

from functools import reduce
def hash_func(str_list, mod=1000):
    '''
    实现一个hash函数，对输入的字符串数组求一个hash值
    未做优化，直接对输入的字符串进行hash
    :param str_list: 输入的字符串数组
    :parm mod: 求模运算的模，越大发生hash碰撞的可能性越小，但开销也大
    '''
    if not mod: # 如果没有指定模，则根据输入字符串的长度确定
        mod = len(str_list) * 100
    # 统一转化成ascii码形式（字符串、数字、其他符号）统统转化成对应的ASCII形式
    digit_list = map(lambda x:ord(x), str_list)
    return reduce(lambda x,y: x*10 + y, digit_list, 0) % mod # 累加、取模


def bruce_match(string, pattern):
    '''
    暴力匹配，逐个字符串匹配
    用于rolling hash的子模块调用：

    输入字符串和指定的模式一样长
    :param string:
    :param pattern:
    :return:
    '''

    # for i in range(len(string)):
    #     if string[i] != pattern[i]: #只要有一个元素不相同，就不匹配
    #         return False
    # return True

    # 也可以写的更pythonic,一行搞定
    return all(map(lambda x, y: x==y, string, pattern))


def rolling_match(string, pattern):
    '''

    :param string: 输入字符串
    :param pattern:  模式
    :return:
    '''
    p = hash_func(pattern)

    for i in range(len(string) - len(pattern)):
        s = hash_func(string[i: i+ len(pattern)])
        if s == p and bruce_match(string[i:len(pattern)], pattern):
            return i # 返回开始匹配的索引

    return False









def main():
    lst = [1, 2, 3, 4]
    str_lst = ['a', 'b', 'A']
    # print(hash_func(lst))
    print(hash_func(str_lst))

    string = list('2359023141526739921')
    pattern = list('31415')
    print(rolling_match(string, pattern))

if __name__ == '__main__':
    main()