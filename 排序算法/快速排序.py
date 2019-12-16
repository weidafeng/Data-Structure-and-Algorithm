# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         快速排序.py
# Author:       wdf
# Date:         11/25/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  快速排序之所以快，是因为使用了分治法
# Usage：
#-------------------------------------------------------------------------------

'''
同冒泡排序一样， 快速排序也属于交换排序 ， 通过元素之间的比较和
交换位置来达到排序的目的。

快速排序则在每一轮挑选一个基准元素， 并让其他比它大的元素移动到
数列一边， 比它小的元素移动到数列的另一边， 从而把数列拆解成两
个部分
'''

# O(nlogn)

def one_step(lst, idx=0):
    ''' 双边循环法，两个指针，从两边向内遍历
    :param lst: 待排序数组
    :param idx:  选定的基准元素的索引，默认为第一个元素
    :return:  大于基准元素的，在数组右边，小于基准元素的，在数组左边
    '''
    pivot = lst[idx]
    i, j = 1, len(lst) - 1
    while i < j:
        print(lst,i,j)
        while lst[idx] < lst[j] and i < j: # 最右边的元素比基准元素大，不需要交换元素，直接把右边的指针向左移动一位
            j -= 1 # 直到找到第一个比基准元素小的元素，退出循环，准备交换
        while lst[idx] > lst[i] and i <j: # 最左边的元素比基准元素小，不需要交换元素，直接把左边的指针向右移动一位
            i += 1# 直到找到第一个比基准元素大的元素，退出循环，准备交换

        # 交换
        # if i < j: # 两个数不相等 ，# 最后一步退出循环前，i=j，交换不交换都行
        lst[j], lst[i] = lst[i], lst[j]

    # 整体交换完成后，把基准元素放到中间位置
    # if lst[idx] > lst[i]:
    lst[i], lst[idx] = lst[idx], lst[i]
    # else:
    #     lst[i-1], lst[idx] = lst[idx], lst[i-1]

    return lst

def one_step2(lst, idx, end):
    ''' 单边循环法，一个指针， 表示小于pivot元素的区域边界
    lst: 待排序数组
    idx： 待排序数组的起始部分索引
    end:  待排序数组的结束部分索引
    '''
    pivot = lst[idx]
    mask = idx # 表示小于pivot元素的区域边界
    for i in range(idx, end):
        print(i,mask, lst)
        if lst[i] >= pivot: # 该元素比基准元素大，则继续遍历
            pass
        else: # 当前元素比基准元素小，则需要两个步骤：
                # 1） mask指针+1（表示比基准元素小的元素多了一个）
                # 2） 把mask移动后的元素与当前元素交换
            mask += 1 # 只是mask指向的位置大于基准元素
            lst[mask], lst[i] = lst[i], lst[mask] # 交换后才满足条件

    # 最后把基准元素交换到mask的位置
    lst[mask], lst[idx] = lst[idx], lst[mask]
    return lst

###############################
# method 2
# 空间复杂度较高
# 一个函数递归实现
'''弊端很明显：
分组基准的选取过于随便，不一定可以取到列表的中间值
空间复杂度大，使用了两个列表解析式，而且每次选取进行比较时需要遍历整个序列。
若序列长度过于小(比如只有几个元素)，快排效率就不如插入排序了。
递归影响性能，最好进行优化。
'''
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]    # 选取中间的元素为基准
    left = [x for x in arr if x < pivot]     # 小于基准元素的，放在左边
    middle = [x for x in arr if x == pivot]    # 等于基准元素的，放在中间
    right = [x for x in arr if x > pivot]     # 大于基准元素的， 放在右边
    return quicksort(left) + middle + quicksort(right)  # 对左边和右边进行递归调用


########################################
# method 2
# https://www.jianshu.com/p/2b2f1f79984e


# 封装函数
def quick_sort(L):
    return q_sort(L, 0, len(L) - 1)

# 递归调用函数
def q_sort(L, left, right):
    print(L)
    if left < right:
        pivot = Partition(L, left, right)
        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

# 具体执行比较、交换的函数（与我写的第一个函数one_step() 功能类似）
# 返回pivot元素的索引
def Partition(L, left, right):
    pivotkey = L[left]  # 默认选最左边的元素
    while left < right:
        while left < right and L[right] >= pivotkey:  # 找到不满足条件的元素（比pivot小的元素）
            right -= 1
        L[left] = L[right]              # 把上面那个大元素放到左边
        while left < right and L[left] <= pivotkey:  # 找到比pivot大的元素
            left += 1
        L[right] = L[left]      # 把上面那个小元素放到右边

    L[left] = pivotkey  # 中间放回pivot
    return left

def main():
    lst = [4,7,6,5,1,8,3,2,1]
    lst2= [4,9,8,7,1,2,3,5]
    import random
    lst = random.sample(range(1,20), 10)
    # print(one_step(lst, 0))
    print(one_step2(lst, 0, len(lst)))
    # print(one_step(list(range(1,10)), 0))

    # print( lst2)
    # print(quick_sort(lst2))
    # quicksort(lst)
    # print( lst)

if __name__ == '__main__':
    main()