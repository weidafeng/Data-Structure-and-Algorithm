#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/6/2020 3:48 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        18. 删除链表的重复节点
# description:      给定一个排好序的链表，删除所有节点（如1233445——34重复——得到125）
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

    # 删除所有重复节点
    def delete_all_duplicate_nodes(self):
        pre, cur = self.head, self.head.next
        if cur is None or cur.next is None:  # 如果链表为空或者只有一个节点，直接返回
            return

        while cur.next:
            val = cur.val
            # 先做一次判断，比较当前元素与后续元素是否重复
            if val != cur.next.val:
                # 不相等，则直接跳过——注意，此时才能把pre往后移动，而不能去除一次重复节点后马上移动，因为下一个节点也可能是需要删除的重复节点
                pre, cur = cur, cur.next
            else:  # 相等，则继续往后比较（考虑多个数重复，如122222345——1345）
                cur = cur.next  # 往后移动一位
                while cur.next and cur.next.val == val:  # 与下下一位比较是否相同
                    cur = cur.next  # 如果还相同，继续往后比较
                cur = cur.next  # 指向不重复的元素（下一个）
                pre.next = cur  # 链接前面的


def main():
    # 新建一个链表
    print("新建一个含有重复元素的链表")
    ll = LinkedList()
    lst = [1, 2, 3, 3, 4, 4, 4, 5]
    for i in lst:
        ll.add_first(i)
    ll.print_lkst()

    print('删除重复元素')
    ll.delete_all_duplicate_nodes()
    ll.print_lkst()


if __name__ == '__main__':
    main()
