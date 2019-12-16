# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         15. three sum.py
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

# 三个数之和等于0
# 返回所有结果

# method 1. using three-layer loops
# O(N^3)
def three_sum(lst, dst=0):
    n = len(lst)
    res = []
    for a in range(n-2):
        for b in range(a+1, n-1):
            for c in range(b+1, n):
                # print(lst[a], lst[b], lst[c])
                if lst[a] + lst[b]+ lst[c]== dst:
                    res.append([lst[a], lst[b], lst[c]])
                    # print(a,b,c)
    return res


# method 2, using map
# 0(N^2)

def three_sum_2(lst, dst=0):
    lst.sort()  # sort
    # print(lst)
    res = set() # store the result
    for i, a in enumerate(lst[:-2]):  # the first loop, iter all nums from the first to the end(but last two)
        if i >= 1 and a == lst[i-1]:  # skip to avoid duplicate
            continue

        d = {} # 使用map，判断a元素之后的所有元素里，是否有两个元素和为dst-a
        for b in lst[i+1: ]:    # the second num
            if b not in d:  # 如果b在d里面，说明b = dst - a - 'b'(这个b是之前的b)，即之前有满足dst-a-当前b的元素
                d[dst - a - b] = 1
            else:
                res.add((a, b, dst-a-b))

    return list(res)


# method 3: two pointers
# O(N^2)

def three_sum_3(lst, dst=0):
    print('method 3')
    lst.sort()
    res = []
    for a in range(len(lst)-1): # loop for all nums
        i, j = a+1, len(lst)-1
        while i < j:
            print(lst[a],lst[i] , lst[j] )
            if lst[a] + lst[i] + lst[j] == dst:
                res.append([lst[a],lst[i],lst[j]])
                i += 1  # next num
            elif lst[a] + lst[i] + lst[j] > dst:
                j -= 1
            else:
                i += 1
    return res


def main():
    lst = [0, -2, 1, 3, 5, -1, 2]
    print(three_sum(lst))
    print(three_sum_2(lst))
    print(three_sum_3(lst))

if __name__ == '__main__':
    main()