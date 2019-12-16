# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         找出数组中重复的元素.py
# Author:       wdf
# Date:         11/19/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
# -------------------------------------------------------------------------------

# 给定一个数组，找出里面重复的元素（只有一组重复）

# method 1. count the sum(only for the 'one duplicate' situation
# O(N)
def find_dup(lst):
    return sum(lst) - sum(set(lst))


# method 2. using dictionary
# O(N)
# 记录每一个元素出现的次数
def find_dup_2(lst):
    dic = {}
    for i, v in enumerate(lst):
        if v in dic:
            dic[v] += 1
        else:
            dic[v] = dic.get(v, 0) + 1  # count the times of duplicate
    return {k: v for k, v in dic.items() if v > 1}  # 筛选，次数大于1的，表示重复

# method 3. brutal loop
# O(N^2)
# 判断当前元素在之前是否出现过
def find_dup_3(lst):
    res = []
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] == lst[j]:
                res.append(lst[i])
    return res


def main():
    lst = [3, 1, 2, 5, 4, 9, 7, 2, 3] # 含有两组重复
    print(find_dup(lst)) # 该方法失效
    print(find_dup_2(lst))
    print(find_dup_3(lst))


if __name__ == '__main__':
    main()
