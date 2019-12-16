# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         计数排序.py
# Author:       wdf
# Date:         11/28/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  适用于元素全是整数的情况
# Usage：
#-------------------------------------------------------------------------------
# 数组中每一个下标位置的值代表数列中对应整数出现的次数。
# 有了这个统计结果， 排序就很简单了。 直接遍历数组， 输出数组元素的
# 下标值， 元素的值是几， 就输出几次。

# 当数列最大和最小值差距过大时， 并不适合用计数排序。
# 当数列元素不是整数时， 也不适合用计数排序。
'''
eg:
lst = [4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10]
count_list = [1, 1, 1, 1, 2, 2, 2, 1, 1, 0, 1]  # 表示0元素出现了1次，1出现1次、……10出现1次
'''
def count_sort(lst, largest=None):
    '''
    :param lst: 待排序数组
    :param largest: 该数组中最大的元素（用于初始化计数数组的长度）
    :return: 
    '''
    largest = largest if largest else max(lst) + 1 # 加1 表示0元素
    count_list = [0] * largest #计数数组，用于统计每个元素出现的次数

    # 得到计数数组
    for i in range(len(lst)):
        count_list[lst[i]] += 1
    # print(count_list)

    # 遍历统计数组， 输出结果
    sorted_list = []
    for i in range(len(count_list)):
        sorted_list += [i] * count_list[i]

    return sorted_list


# 优化, 对于如下所示的数组，如果用max作为计数数组长度，会很浪费
# [95， 94， 91， 98， 99， 90， 99， 93， 91， 92]
def count_sort_2(lst, smallest= None, largest=None):
    '''
    :param lst: 待排序数组
    :param largest: 该数组中最大的元素（用于初始化计数数组的长度）
    :return:
    '''
    largest = largest if largest else max(lst) + 1
    smallest = smallest if smallest else min(lst)
    count_list = [0] * (largest - smallest) #计数数组，用于统计每个元素出现的次数

    # 得到计数数组
    for i in range(len(lst)):
        count_list[lst[i]- smallest] += 1
    # print(count_list)

    # 遍历统计数组， 输出结果
    sorted_list = []
    for i in range(len(count_list)):
        sorted_list += [i +  smallest] * count_list[i]  # 元素i出现了count_list[i]次

    return sorted_list

def main():
    import random
    lst = [4,4,6,5,3,2,8,1,7,5,6,0,10]
    print(lst)
    print(count_sort_2(lst))


if __name__ == '__main__':
    main()