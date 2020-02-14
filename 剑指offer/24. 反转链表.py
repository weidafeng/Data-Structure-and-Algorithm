#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/6/2020 10:07 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        24. 反转链表
# description:      翻转链表，并输出翻转后链表的头结点
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

    # 翻转链表
    def reverse(self):
        # 没有节点
        if self.head is None:
            return None
        # 只有一个节点,翻转不反转都一样
        elif self.head.next is None:
            return self.head
        if self.head.next.next is None:
            return False
        pre, cur = None, self.head.next
        while cur:
            if cur.next:
                nxt = cur.next  # 临时保存下一个节点，防止丢失
                cur.next = pre
                pre = cur
                cur = nxt
            else:  # cur已经到最后一个节点，没有后继节点了
                self.head = Node()
                self.head.next = cur
                cur.next = pre
                break
        return cur, cur.val  # 返回翻转后的头结点（不含head)


def main():
    # 新建一个链表
    print("新建一个链表")
    ll = LinkedList()
    for i in range(10):
        ll.add_first(i)
    ll.print_lkst()

    print('翻转链表')
    print(ll.reverse())
    ll.print_lkst()



if __name__ == '__main__':
    main()
