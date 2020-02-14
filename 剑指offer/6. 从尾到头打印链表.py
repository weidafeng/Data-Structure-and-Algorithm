#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/20/2020 11:12 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        6. 从尾到头打印链表
# description:      逆序打印
# usage:            


class Node():
    def __init__(self, value=None, next=None):
        self.data = value
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
            print(node.data, end=' ')
            node = node.next
        print()


    # 倒序打印链表（不修改链表）
    def reverse_print(self):
        # 方法一，借助堆栈，先进后出
        stack = []
        cur_node = self.head.next
        while cur_node:
            stack.append(cur_node.data)
            cur_node = cur_node.next
        while stack:
            print(stack.pop(), end=' ')
        print()


    # 倒序打印链表（不修改链表）
    def reverse_print_2(self):
        # 方法二，上面用了堆栈实现，而递归本质上就是一种栈结构
        cur_node = self.head.next
        self._reverse_recursive_helper(cur_node)

    # 递归调用的辅助函数
    # 要想实现倒序打印，则每访问到一个节点时，先递归地打印他的后继节点，再打印当前节点本身
    def _reverse_recursive_helper(self, cur_node):
        if cur_node and cur_node.next:
            self._reverse_recursive_helper(cur_node.next)
        print(cur_node.data, end=' ')

def main():
    print("测试linked list： ")
    lkst = LinkedList()
    print(lkst)  # linked list
    print(lkst.head)  # node
    print()

    # 开始添加元素
    print("开始添加元素(first)")
    lkst.add_first(10)
    lkst.print_lkst()
    lkst.add_first(20)
    lkst.print_lkst()
    lkst.add_first(30)
    lkst.add_first(40)
    lkst.add_first(50)
    print("正序输出：")
    lkst.print_lkst()
    print("倒序输出：")
    lkst.reverse_print()
    print("倒序输出-2：")
    lkst.reverse_print_2()
    print()


if __name__ == '__main__':
    main()
