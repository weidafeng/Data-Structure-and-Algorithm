# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         堆排序.py
# Author:       wdf
# Date:         11/28/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  需要从小到大排序， 则构建成最大堆；
#               需要从大到小排序， 则构建成最小堆。
# 以最大堆为例， 如果删除一个最大堆的堆顶（并不是完全删除， 而是跟
# 末尾的节点交换位置） ， 经过自我调整， 第2大的元素就会被交换上
# 来， 成为最大堆的新堆顶。
#
# 删除到最后的结果是，最大的元素在最后面，最小的元素在最前面——完成从小到大排序
# Usage：
#-------------------------------------------------------------------------------
#
# 堆排序算法的步骤。
# 1. 把无序数组构建成二叉堆。
# 2. 循环删除堆顶元素， 并将该元素移到集合尾部， 调整堆产生新的堆顶。
# 第1步， 把无序数组构建成二叉堆， 这一步的时间复杂度是O(n) 。
# 第2步， 需要进行n-1次循环。 每次循环调用一次downAdjust方法， 所以
# 第2步的计算规模是 (n-1)×logn ， 时间复杂度为O(nlogn) 。
# 两个步骤是并列关系， 所以整体的时间复杂度是O(nlogn)

# 与快速排序的不同点：
# 快速排序的最坏时间复杂度是O(n^2 ) ， 而堆排序的最坏时间复杂度稳定在O(nlogn) 。

# 相同点：
# 平均时间复杂度都是O(nlogn) ， 并且都是不稳定排序


def maintain(lst, parent_idx, length):
    '''
    对根节点（parent_idx)进行下沉调整，保证根节点比其所有儿子节点都大
    :param lst: 带调整的堆（以数组形式存储）
    :param parent_idx: 要下沉调整的根节点
    :param length: 数组长度（用于判断边界条件）
    :return:
    '''
    tmp = lst[parent_idx] # 保存父亲节点的值，用于后面交换
    child_idx = 2 * parent_idx + 1 # 左儿子的索引

    while child_idx < length:
        # 找出左儿子、右儿子（如有）中的最大值
        if (child_idx + 1 < length) and (lst[child_idx] < lst[child_idx + 1]): # 如果右儿子存在，且比左儿子大
            child_idx += 1 # 指向右儿子

        if lst[parent_idx] >= lst[child_idx]: # 根节点最大，无需交换，退出
            break

        # 交换（单向赋值即可，无需真正交换元素）
        lst[parent_idx] = lst[child_idx]  # 根节点存储最大的值
        # 下一层
        parent_idx = child_idx
        child_idx = 2* parent_idx + 1

    # 最后把原先根节点的值赋给最后的儿子节点
    lst[parent_idx] = tmp



def heap_sort(lst):
    # 第一步，把无序数组调整为最大堆(只能保证根节点的元素最大）
    last_parent_idx = (len(lst) - 2) // 2 # 最底层的最后一个父亲节点
    for i in range(last_parent_idx):
        maintain(lst,len(lst) - i - 1, len(lst))
        print("heapify:", lst)
    # for i in range(last_parent_idx, -1, -1):  # 注意，必须使用一个循环，从底部开始向上遍历到堆顶，不然无法保证堆顶是最大的元素
    #     maintain(lst, i, len(lst))
    # 第二步， 循环删除堆顶元素， 移到集合尾部， 调整堆产生新的堆顶
    for i in range(len(lst)-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i] # 堆顶元素与最后一个元素交换
        # 调整最大堆，保证堆顶元素最大
        maintain(lst, 0, i)
    return lst

# ###################################################3

from collections import deque
def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L


def heap_adjust(L, start, end):
    temp = L[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp


def heap_sort_2(L):
    L_length = len(L) - 1

    first_sort_count = L_length // 2
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)
        print("heapify:", L)

    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)

    return [L[i] for i in range(1, len(L))]

##############################################
# 递归实现
def heapify(arr, n, i):
    largest = i  # 当前父亲节点为最大的元素
    l = 2 * i + 1  # left = 2*i + 1 
    r = 2 * i + 2  # right = 2*i + 2

    # 找到最大的节点
    # 其中 l<n 也是递归终止的条件
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    # 如果有比当前父亲节点更大的元素
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)  # 递归调用


def heapSort(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n, -1, -1):  # 从最后一个元素开始，逐个往前、往上遍历，调整堆
        heapify(arr, n, i)
    # 此时，已经满足最大堆的形式：每个根节点都比其左右子树的任意儿子大
        print("heapify:", arr)
    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0) # 每次取出堆顶最大值后，需要再调整一次，找到
    return arr


def main():
    # import random
    # lst = random.sample(range(1, 20), 9)
    # print(lst)
    # # lst = maintain(lst, 0, len(lst))
    # print(heap_sort(lst))
    # print(lst)
    lst = [10, 8, 12, 17, 16, 2, 1, 6, 3]
    print(lst)
    print(heap_sort(lst))
    print()
    lst = [10, 8, 12, 17, 16, 2, 1, 6, 3]
    print(heapSort(lst))
    print()
    lst = [10, 8, 12, 17, 16, 2, 1, 6, 3]
    lst.insert(0, 0)
    print(heap_sort_2(lst))
    # L = deque([10, 8, 12, 17, 16, 2, 1, 6, 3])
    # L.appendleft(0)
    # print(heap_sort_2(L))




if __name__ == '__main__':
    main()