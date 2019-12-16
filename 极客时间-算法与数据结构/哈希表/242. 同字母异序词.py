# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         242. 同字母异序词.py
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

# 同字母异序词
# 如cat， act

# 方法一，两个字符串排序
# O(N(log(N))
def anagram_1(s, t):
    return sorted(s) == sorted(t)

# method 2
# dictionary
# O(N)
def anagram_2(s,t):
    s_dic, t_dic = {}, {}
    for i in s:
        s_dic[i] = s_dic.get(i, 0) + 1
    for j in t:
        t_dic[j] = t_dic.get(j, 0) + 1
    return s_dic == t_dic

# method 3
# build a sample dictionary
# O(N)
def anagram_3(s,t):
    s_dic, t_dic = [0] * 26, [0] * 26  # store the number of alphabeta
    for i in s:
        s_dic[ord(i) - ord('a')] += 1
    for j in t:
        t_dic[ord(j) - ord('a')] += 1
    return s_dic == t_dic




def main():
    s = 'cat'
    t = 'act'
    print(anagram_1(s,t))
    print(anagram_2(s,t))
    print(anagram_3(s,t))


if __name__ == '__main__':
    main()