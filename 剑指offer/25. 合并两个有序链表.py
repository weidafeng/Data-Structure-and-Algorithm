#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/6/2020 10:47 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        25. 合并两个有序链表
# description:      给定两个有序链表，要求合并之后仍然有序
# usage:            
# 如 1357  2468
# 合并之后 12345678

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# 递归实现
# 合并两个有序链表
def merge_two_ordered_lkst(lkst_1, lkst_2):
    # 如果其中一个为空
    if lkst_1 is None:
        return lkst_2
    if lkst_2 is None:
        return lkst_1

    merge_node = None

    # 以lkst_1 为主链（即把lkst_2合并到lkst_1上）
    if lkst_1.val <= lkst_2.val:
        merge_node = lkst_1
        merge_node.next = merge_two_ordered_lkst(lkst_1.next, lkst_2)
    else:
        merge_node = lkst_2
        merge_node.next = merge_two_ordered_lkst(lkst_1, lkst_2.next)
    return merge_node


def print_lkst(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


def main():
    # 新建一个链表
    print("新建一个链表")
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(7)
    node5 = Node(9)

    lkst_1 = node1
    lkst_1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    print(lkst_1)
    print_lkst(lkst_1)

    print("新建一个链表")
    node1 = Node(2)
    node2 = Node(4)
    node3 = Node(6)
    node4 = Node(8)
    node5 = Node(10)

    lkst_2 = node1
    lkst_2.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    print(lkst_2)
    print_lkst(lkst_2)

    merge = merge_two_ordered_lkst(lkst_1, lkst_2)
    print(merge)
    print_lkst(merge)


if __name__ == '__main__':
    main()
