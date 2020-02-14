#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/6/2020 9:04 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        22. 链表的倒数第k个节点
# description:      输入一个链表，输出倒数第k个节点的值
# usage:            


class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = Node()  # 链表初始化，只有一个头结点
        self.length = 0

    def add_first(self, data):
        '''从头添加元素'''
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1

    # 打印链表
    def print_lkst(self):
        node = self.head.next  # 不打印头结点
        # print("head: ",head_node, head_node.data)
        while node != None:
            print(node.val, end=' ')
            node = node.next
        print()

    # 输出倒数第k个节点的值
    def find_kth_to_the_tail(self, k):
        # 方法： 快慢两个指针
        # 快指针先走k-1步，慢指针才开始走
        # 当快指针走到最后，慢指针指向倒数第k个节点

        # 需要注意几个边界条件
        # 1. 空链表
        # 2. k = 0 or k = len(lst)
        # 3. k > len(lst)

        head = self.head.next

        # 链表为空 或者 k为0
        if head is None or k == 0:
            return None

        # 快指针(head)先走 k-1 步
        while k - 1:
            if head.next is None:  # 链表没有那么多元素
                return None
            head = head.next
            k -= 1

        # 快慢指针同时走, 直到快指针走到末尾
        slow = self.head.next
        while head.next:
            head = head.next
            slow = slow.next

        return slow.val


def main():
    # 新建一个链表
    print("新建一个链表")
    ll = LinkedList()
    for i in range(10):
        ll.add_first(i)
    ll.print_lkst()

    print('查找倒数第k个元素')
    print(ll.find_kth_to_the_tail(0))
    print(ll.find_kth_to_the_tail(1))
    print(ll.find_kth_to_the_tail(2))
    print(ll.find_kth_to_the_tail(9))
    print(ll.find_kth_to_the_tail(90))


if __name__ == '__main__':
    main()
