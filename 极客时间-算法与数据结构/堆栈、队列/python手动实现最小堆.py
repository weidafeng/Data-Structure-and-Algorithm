# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         python手动实现最小堆.py
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
'''
参考：
原理： https://www.jianshu.com/p/d174f1862601
代码： https://blog.csdn.net/qq_40587575/article/details/89290135

'''
# 最小堆
class MinHeap(object):
    def __init__(self,max_size=None):
        self.max_size = max_size
        self.lst = [None] * self.max_size
        self.count = 0

    def length(self):
        return self.count

    def show(self):
        for i in range(self.length()):
            print(self.lst[i], end=' ')

    def add(self, value):
        '''添加元素，保证最上面是最小的元素'''
        if self.length() >= self.max_size:
            self.lst.extend([None] * self.max_size)
            self.max_size *= 2

        # 插入到最后一位
        self.lst[self.length()] = value
        # 上移调整
        self._shift_up(self.length())
        self.count += 1

    def _shift_up(self, index):
        parent = (index - 1) //2
        if index: # 大于0 ，递归终止条件
            if self.lst[parent] > self.lst[index]: # 需要交换
                self.lst[parent], self.lst[index] = self.lst[index], self.lst[parent]
                self._shift_up(parent)


    def extract(self):
        '''删除元素，保证每次弹出的都是最小的元素'''
        value = self.lst[0] # 要弹出的元素（堆顶）
        self.count -= 1 # 元素数减去一
        # 把最后面的元素放到堆顶，保证完全二叉树的形状
        self.lst[0] = self.lst[self.length()]
        # 从上往下，调整
        self._down_shift(0)
        return value

    def _down_shift(self, index):

        # 找到两个儿子节点
        left = index * 2 + 1
        right = index * 2 + 2
        cur_smallest = index # 临时变量，储存最小元素的索引

        # 找到根节点与两个儿子节点中最小的元素
        if left < self.length() and self.lst[cur_smallest] > self.lst[left]:
            cur_smallest = left
        if right < self.length() and self.lst[cur_smallest] > self.lst[right]:
            cur_smallest = right

        if cur_smallest != index:  # 需要交换
            self.lst[cur_smallest], self.lst[index] = self.lst[index], self.lst[cur_smallest]

            self._down_shift(cur_smallest)

def main():
    import numpy as np
    length = 3
    num = np.random.randint(low=1, high=20,size=length)
    print("num: ", num)

    print("init the heap: ")
    min_heap = MinHeap(length) # 实例化一个最大长度为5的最大堆
    print(min_heap.length(), min_heap.max_size)
    min_heap.show()
    print()

    print('add num to the heap:')
    for i in num:
        min_heap.add(i)
    print(min_heap.length(), min_heap.max_size)
    min_heap.show()
    print()

    print("out of range：")
    min_heap.add(100)
    print(min_heap.length(), min_heap.max_size)
    min_heap.show()


    print()
    print('remove num from the heap')
    for i in range(length):
        print(min_heap.extract(), end=' ')



if __name__ == '__main__':
    main()