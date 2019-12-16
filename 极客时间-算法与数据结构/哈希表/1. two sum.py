# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         1. two sum.py
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


# 1, two sum
# method 1, two-layer loop

# method 2. two-pointers

# method 3. map
def two_sum(lst, dst=0):
    res= []
    dic = {}
    
    for i in range(len(lst)):
        if  lst[i] in dic:
            res.append([i, dic[lst[i]]])
        else:
            dic[dst-lst[i]] = i
    print(dic)
    return res


# reformulation
def two_sum_2(lst, dst=0):
    dic = {}
    res = []
    for i, v in enumerate(lst):
        if v in dic:
            res.append([i, dic[v]])
        else:
            dic[dst-v] = i  # 如果v在dic里，说明之前出现过数x，使得x+v=dst——其中一个解
    return res

def main():
    lst = [0, -2, 1, 3, 5, -1, 2]
    print(two_sum(lst))
    print(two_sum_2(lst))

if __name__ == '__main__':
    main()