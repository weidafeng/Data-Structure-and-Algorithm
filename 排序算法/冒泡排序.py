# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         冒泡排序.py
# Author:       wdf
# Date:         11/25/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  依次比较相邻的两个元素——每次循环可以把最大的元素移动到最后面
# Usage：
# -------------------------------------------------------------------------------

# version 1. 最原始的冒牌排序
# O(N^2)
def bubble_sort_v1(lst):
    for i in range(len(lst)):  # 遍历每一个元素（循环的轮数）
        for j in range(0, len(lst) - i - 1):  # 每次循环比较相邻的两个元素
            if lst[j] > lst[j + 1]:  # 需要交换
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# version 2
# 有些情况，经过第x轮排序后， 整个数列已然是有序的了。
# 排序算法仍然兢兢业业地继续执行了完len(lst)轮排序。
# 在这种情况下， 如果能判断出数列已经有序， 并做出标记， 那么剩下的
# 几轮排序就不必执行了， 可以提前结束工作。

# 通过设置boolean变量来判断某次循环是否没有出现交换，说明排序已完成，可以返回。
def bubble_sort_v2(lst):
    for i in range(len(lst)):  # 遍历每一个元素（循环的轮数）
        flag = True  # 初始时假定数组已经有序，不需要进行交换
        for j in range(0, len(lst) - i - 1):  # 每次循环比较相邻的两个元素
            if lst[j] > lst[j + 1]:  # 需要交换
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                flag = False  # 进行了交换
        if  flag:  # 上次循环中，没有进行元素交换（说明已经有序）
            break
    return lst

'''error
# version 3.
# 如[3,4,2,5,6,7,8,9]  # 后面数组已经有序，不需要再遍历、比较、交换
# 原始冒泡排序默认遍历len(n)次，每次遍历结束保证最后n个元素有序
# 但有时候遍历x次后，会有多余x个元素已经有序——不需要再遍历

# 设置一个索引，表示遍历第i次时，已经有序的元素个数

# 在每一轮排序后， 记录下来最后一次元素交换的位置，
# 该位置即为无序数列的边界， 再往后就是有序区了
def bubble_sort_v3(lst):
    for i in range(len(lst)):  # 遍历每一个元素（循环的轮数）
        flag = True  # 初始时假定数组已经有序，不需要进行交换
        ordered_index = 0 # 设置一个索引，表示遍历第i次时，已经有序的元素个数
        for j in range(0, len(lst) - i - 1):  # 每次循环比较相邻的两个元素
            if lst[j] > lst[j + 1]:  # 需要交换
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                flag = False  # 进行了交换
                ordered_index = j
            if j > len(lst) - i - 1 - ordered_index:
                break
        if  flag:  # 上次循环中，没有进行元素交换（说明已经有序）
            break
    return lst
'''

def main():
    import random
    lst1 = [5,8,6,3,9,2,1,7]
    print(lst1)
    print(bubble_sort_v1(lst1))
    lst2 = [5,8,6,3,9,2,1,7]
    print(bubble_sort_v2(lst2))
    lst = [3,4,2,5,6,7,8,9]  # 后面数组已经有序，不需要再遍历、比较、交换
    lst3 = random.sample(range(20), 10)
    print(lst3)
    # print(bubble_sort_v3(lst3))


if __name__ == '__main__':
    main()
