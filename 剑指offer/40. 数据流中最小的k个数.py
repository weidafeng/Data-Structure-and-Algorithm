#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/9/2020 5:55 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        40. 数据流中最小的k个数
# description:      给出海量数据中最小的k个数
# usage:            


# 最简单的方法是排序、输出前k个数，复杂度为O(nlogn)
# 但数据量太大，或者是数据流的形式时，不能用排序

# 考虑堆
# 设置一个大小为k的数据容器——最大堆——而非最小堆
# 每次从数据流中读取一个数n
#     如果堆中数据不够k个，则直接插入
#     如果堆已满，则只能替换——把最大的元素删除、插入新的元素——所以需要最大堆


# 方法一， 用heapq库函数的nsmallest方法
def k_smallest_numbers(lst, k):
    # 堆的内置函数
    import heapq
    # heapq.heapify(lst)
    return heapq.nsmallest(k, lst)


# 方法二，调用heapq库函数，但显示地写明实现思路
def k_largest_numbbers(lst, k):
    '''
    求输入序列中最 **大** 的k个数
    遍历输入序列
        如果结果不满k，则直接加入
        如果结果满k，则比较、删除较大的数、添加较小的数
    :param lst:
    :param k:
    :return:
    '''
    import heapq
    heapq.heapify(lst)  # in-place， 构造堆——heapq只支持最小堆（堆顶元素最小）
    res = []  # 存储结果
    for i in range(len(lst)):
        if len(res) < k:  # 如果还没有够K个数，可以直接插入
            res.append(lst[i])
            heapq.heapify(res)  # maintain 最小堆，堆顶为最小的元素
        else:  # 如果超过了k个元素，则需要替换
            if res[0] < lst[i]:  # 如果新插入的元素更大，则替换
                res[0] = lst[i]
                heapq.heapify(res)  # 重新 maintain 最小堆，堆顶为最小的元素
            else:  # 如果新插入的元素太小，则无需操作
                continue
    return res


# 方法三， 手动实现最大堆，容量为k
class MaxHeap(object):
    '''python 实现最大堆
    最大堆、最小堆是完全二叉树，可以用数组实现'''

    def __init__(self, max_size=None):
        '''
        :param max_size: 数组最大长度——要求的最小的元素个数（如果超出长度了，则替换）
        :param lst : 用数组存储堆的元素
        :param count :   堆里的元素个数
        '''
        self.max_size = max_size
        self.lst = [None] * max_size
        self.count = 0

    def length(self):
        return self.count

    def show(self):
        print('print the heap: ', end='')
        if self.count <= 0:
            print('NULL')
        print(self.lst[: self.count], end=' ')

    def add(self, value):
        '''
        保证最大的元素总是在最上面，根节点总是比其左右儿子节点大

        往最大堆里插入元素， 步骤如下：
        先插入到最后一个位置
        然后依次与其父节点比较大小：
            如果当前节点比其父节点大——交换位置
            如果当前节点比其父节点小——不变，完成上浮操作

        :param value:  待插入的值
        :return:
        '''
        if self.count >= self.max_size:  # 判断是否越界
            # 如果已经有k个数了，则替换
            if self.lst[0] > value:  # 如果新插入的元素更小，则替换
                self.lst[0] = value
                self._shift_down(0)  # 替换后，从顶到底，维护堆，保证堆顶元素最大
            # 如果插入的元素比当前最大值要大，则无需操作
        else:
            # 如果没有越界，则直接插入，并维护堆，保证堆顶元素最大
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
        if index > 0:  # 递归的终止条件
            parent = (index - 1) // 2
            if self.lst[index] > self.lst[parent]:  # 当前节点更大，需要上移(交换两个元素）
                self.lst[parent], self.lst[index] = self.lst[index], self.lst[parent]
                self._shift_up(parent)  # 递归调用，比较上移之后的节点，与其父节点
            # 如果插入的元素小于其根节点，则不需要操作

    # 未使用该函数
    def extract(self):
        '''
        弹出最大的元素
        保证每次弹出的总是最大的元素，下面的大小关系不保证

        删除最大的元素， 步骤如下：
        先去除最上面的元素（最大）
        把最后面的元素放到堆顶（保持完全二叉树的形状）
        然后比较最上面的元素与其左右儿子，通过交换，把最大的放在上面
        '''
        if self.count <= 0:  # 判断堆里面是否还有元素
            raise Exception('No value in this heap!')

        value = self.lst[0]  # 要弹出的最大的元素（堆顶）
        self.count -= 1  # 长度减一
        self.lst[0] = self.lst[self.count]  # 把最后面的元素放到最上面
        self._shift_down(0)  # 递归调用，从上往下、逐层下沉，把当前最大的元素放到最上面
        return value  # 返回弹出的最大值

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

        if tmp_largest != index:  # 交换
            self.lst[index], self.lst[tmp_largest] = self.lst[tmp_largest], self.lst[index]

            # 然后递归（如果上一步没有交换，说明此后就无需交换）
            self._shift_down(tmp_largest)


def main():
    lst = [4, 5, 1, 6, 2, 7, 3, 8, 0]
    print(k_smallest_numbers(lst, 4))

    # 测试nsmallest
    vals = []
    import heapq
    for val in lst:
        vals.append(val)
        print(heapq.nsmallest(3, vals))

    print('*' * 10)
    print('测试nlargest')
    lst = [4, 5, 1, 6, 2, 7, 3, 8, 0]
    print(lst)
    print(k_largest_numbbers(lst, 3))
    print('*' * 10)
    print('测试手动实现的最大堆')
    lst = [4, 5, 1, 6, 2, 7, 3, 8, 0]
    my_heap = MaxHeap(3)
    for v in lst:
        my_heap.add(v)
        my_heap.show()
        print()


if __name__ == '__main__':
    main()
