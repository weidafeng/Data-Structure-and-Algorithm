#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/6/2020 3:48 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        18. 删除链表的指定节点
# description:      给定一个单向链表和指定节点，删除该节点
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

    def delete_specific_node_1(self, target):
        ''' 为了方便，我们给的是待删除的节点的数值（假定链表每个元素都不相同） '''
        # 方法一
        # 因为是单向链表，想要删除某节点，需要遍历找到该节点
        # 设置两个指针，一个指向当前节点 cur，另一个指向前一个节点 pre，
        # pre.next = cur.next; del cur;

        if self.head.next is None:  # 链表为空，不含目标元素
            print('No target val in the linked list')
            return False
        pre, cur = self.head, self.head.next
        while cur:
            # 找到待删除节点
            if cur.val == target:
                pre.next = cur.next
                del cur
                return True
            else:  # 未找到，往后移动一位
                pre, cur = cur, cur.next
        return False

    def delete_specific_node_2(self, target):
        # 方法二
        # 上面用了两个指针，能不能只用一个指针？
        # 可以！
        # 遍历、找到待删除节点 cur， 把后面的元素的值赋给待删除的节点，然后把当前指针指向下下一个节点
        if self.head.next is None:  # 链表为空，不含目标元素
            print('No target val in the linked list')
            return False
        cur = self.head.next

        while cur:
            # 如果找到了，
            if cur.val == target:
                if cur.next is None:  # 如果待删除的节点是否为最后一个节点，只能从头遍历、找到前一个节点
                    node = self.head.next
                    while node.next.next:
                        node = node.next
                    node.next = None  # 删除最后一个节点（赋值为None）
                else:  # 不是最后一个节点，则把后面的元素的值赋给待删除的节点，然后把当前指针指向下下一个节点
                    cur.val = cur.next.val
                    cur.next = cur.next.next
                return True
            else:
                cur = cur.next

def main():
    # 新建一个链表
    print("新建一个链表")
    ll = LinkedList()
    for i in range(10):
        ll.add_first(i)
    ll.print_lkst()

    print('删除元素')
    print(ll.delete_specific_node_1(0))
    # print(ll.delete_specific_node_2(8))
    ll.print_lkst()

if __name__ == '__main__':
    main()
