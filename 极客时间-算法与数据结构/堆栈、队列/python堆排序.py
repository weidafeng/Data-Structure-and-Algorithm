# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         python堆排序.py
# Author:       wdf
# Date:         11/24/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

# 构建一个最大堆，实现堆排序

# 维护堆， 把最大的元素放到最前面
def maintain_heap(lst, length, parent):
    left = 2* parent + 1
    right = 2*parent + 2
    cur_largest = parent
    if left < length and lst[left] > lst[cur_largest]:
        cur_largest = left
    if right < length and lst[right] > lst[cur_largest]:
        cur_largest = right

    if cur_largest != parent:
        lst[cur_largest], lst[parent] = lst[parent],lst[cur_largest]
        maintain_heap(lst, length, cur_largest)


# 第一步，构建最大堆
def build_heap(lst):
    # 每一个元素都是从最后插入
    n = len(lst)
    parent = (n - 1) // 2 # 找到他的父亲节点
    for i in range(parent, -1, -1): # 倒序
        maintain_heap(lst, n, i)



def heap_sort(lst):
    # 构造堆
    build_heap(lst)
    n = len(lst)
    for i in range(n-1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0] # 把最大值放在最后面
        maintain_heap(lst, i, 0)

    return lst




def main():
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    print(a)
    print(heap_sort(a))
    alist = [2, 4, 1, 2, 5, 58, 45, 24, 67]
    print(alist)
    print(heap_sort(alist))
    import random
    b = [random.randint(1,1000) for i in range(1000)]
    print(b)
    print(heap_sort(b))


if __name__ == '__main__':
    main()