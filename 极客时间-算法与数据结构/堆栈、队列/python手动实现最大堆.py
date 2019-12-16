# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         python手动实现最大堆.py
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
# 最大堆
class MaxHeap(object):
    '''python 实现最大堆
    最大堆、最小堆是完全二叉树，可以用数组实现'''
    def __init__(self, max_size=None):
        '''

        :param max_size: 数组最大长度（限定资源，如果超出长度了，可以二倍扩充
        : lst : 用数组存储堆的元素
        : count :   堆里的元素个数
        '''
        self.max_size = max_size
        self.lst = [None] * max_size
        self.count = 0

    def length(self):
        return self.count

    def show(self):
        if self.count <= 0:
            print('NULL')
        print(self.lst[: self.count], end=' ')

    def add(self, value):
        ''' 保证最大的元素总是在最上面，下面的大小关系不保证

        往最大堆里插入元素， 步骤如下：
        先插入到最后一个位置
        然后依次与其父节点比较大小：
            如果当前节点比父节点大——交换位置
            如果当前节点比父节点小——不变，完成上浮操作

        注意，只能保证最大的元素在最上面，下面的堆的特性没有考虑
        :param value:  待插入的值
        :return:
        '''
        if self.count >= self.max_size: # 判断是否越界
            # raise Exception('The list is full')

            # 可以把list长度翻倍，原lst元素移动到新list
            print("double the max length")
            self.lst.extend([None] * self.max_size)
            self.max_size *= 2

        # 开始插入
        ## 先插到最后一个位置
        self.lst[self.count] = value
        ## 从最后一个元素、最后一层开始，逐层上移（递归实现）
        self._shift_up(self.count)

        ## 插入完成后，记得长度+1
        self.count += 1

    def _shift_up(self, index):
        '''往最大堆中插入元素，逐层上移比较, 递归实现'''
        # 第一步， 找到当前节点（index），与其父节点（index-1)//2
        # 因为本次实现使用了index = 0 的节点，所以父节点为 （index - 1）//2
        # 如果没有使用index = 0的节点，则父节点为index // 2
        if index > 0: # 递归的终止条件
            parent = (index -1) // 2
            if self.lst[index] > self.lst[parent]: # 当前节点更大，需要上移(交换两个元素）
                self.lst[parent], self.lst[index] = self.lst[index], self.lst[parent]
                self._shift_up(parent)  # 递归调用，比较上移之后的节点，与其父节点

    def extract(self):
        '''保证每次弹出的总是最大的元素，下面的大小关系不保证

        删除最大的元素， 步骤如下：
        先去除最上面的元素（最大）
        把最后面的元素放到堆顶（保持完全二叉树的形状）
        然后比较最上面的元素与其左右儿子，通过交换，把最大的放在上面
        '''
        if self.count <= 0:  # 判断堆里面是否还有元素
            raise Exception('No value in this heap!')

        value = self.lst[0] # 要弹出的最大的元素（堆顶）
        self.count -= 1 # 长度减一
        self.lst[0] = self.lst[self.count] # 把最后面的元素放到最上面
        self._shift_down(0) # 递归调用，从上往下、逐层下沉，把当前最大的元素防抖最上面
        return value # 返回弹出的最大值

    def _shift_down(self, index):
        '''
        下沉，递归调用
        给定一个节点index
        找出他的左右儿子节点
        找出index节点与左右儿子节点中的最大值，通过交换，把最大值放到最上面
        :param index: 要下沉的元素的索引（父亲节点）
        :return:
        '''
        left = index * 2 + 1
        right = index * 2 + 2
        tmp_largest = index
        if left < self.length() and self.lst[left] > self.lst[tmp_largest]:
            # 1. 未越界； 2. 当前节点比儿子他的左儿子节点更小（需要交换）
            tmp_largest = left
        if right < self.length() and self.lst[right] > self.lst[tmp_largest]:
            # 1. 未越界； 2. 右儿子最大
            tmp_largest = right

        if tmp_largest != index: # 交换
            self.lst[index], self.lst[tmp_largest] = self.lst[tmp_largest], self.lst[index]

            # 然后递归（如果上一步没有交换，说明此后就无需交换）
            self._shift_down(tmp_largest)


def main():
    import numpy as np
    length = 3
    num = np.random.randint(low=1, high=20,size=length)
    print("num: ", num)

    print("init the heap: ")
    max_heap = MaxHeap(length) # 实例化一个最大长度为5的最大堆
    print(max_heap.length(), max_heap.max_size)
    max_heap.show()
    print()

    print('add num to the heap:')
    for i in num:
        max_heap.add(i)
    print(max_heap.length(), max_heap.max_size)
    max_heap.show()
    print()

    print("out of range：")
    max_heap.add(100)
    print(max_heap.length(), max_heap.max_size)
    max_heap.show()


    print()
    print('remove num from the heap')
    for i in range(length):
        print(max_heap.extract(), end=' ')



if __name__ == '__main__':
    main()