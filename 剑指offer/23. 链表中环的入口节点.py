#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/6/2020 9:26 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        23. 链表中环的入口节点
# description:      找出链表中环的入口节点
# usage:            

# 1. 判断是否有环
#   - 设置快慢两个指针，一个每次走两步，另一个每次走一步
#   - 如果存在环，则慢指针一定会在环内追上快指针
#   - 如果直到快指针走到最后(next=None)，慢指针也没有追上，则说明不存在环

# 2. 判断环内有几个节点
#   - 上面快慢两个指针一定会在环内相遇
#   - 慢指针从相遇点开始遍历，直到回到出发点
#   - 遍历的次数即为环内的节点数（n）

# 3. 找出环的入口节点
#   - 仍旧设置两个指针，从头结点开始，一个先走n步，另一个才开始走
#   - 两个节点第一次相遇，即为环的入口节点

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

    def cread_ring_node(self, val):
        '''
        测试用，创建一个环
        以值为val的节点作为环的入口节点
        方法：
        找到值为val的节点（确保有该节点），把尾节点指向该节点
        '''
        node = self.head.next
        entry_node = None
        while node.next:  # 遍历到最后
            if node.val == val:
                entry_node = node
            node = node.next
        # 此时，node为最后一个节点，entry_node 为设置的环入口节点
        node.next = entry_node  # 连成环
        print('设置的{}为环节点，地址为{}'.format(val, entry_node))

    # 打印链表
    def print_lkst(self):
        node = self.head.next  # 不打印头结点
        # print("head: ",head_node, head_node.data)
        while node != None:
            print(node.val, end=' ')
            node = node.next
        print()


    # 1. 判断是否有环
    #   - 设置快慢两个指针，一个每次走两步，另一个每次走一步
    #   - 如果存在环，则慢指针一定会在环内追上快指针
    #   - 如果直到快指针走到最后(next=None)，慢指针也没有追上，则说明不存在环
    def has_ring(self):
        '''
        如果存在环，则返回true 和 meeting_node
        如果不存在环，返回False 和 None
        '''
        slow, fast = self.head, self.head.next
        while fast.next:  # 快节点走到末尾
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next

            if slow.val == fast.val:  # 相遇，存在环
                return True, slow

        return False, None

    # 2. 判断环内有几个节点
    #   - 上面快慢两个指针一定会在环内相遇
    #   - 慢指针从相遇点开始遍历，直到回到出发点
    #   - 遍历的次数即为环内的节点数（n）
    def count_rings(self):
        has_ring, meeting_node = self.has_ring()
        if not has_ring:
            return 0
        meeting_val = meeting_node.val
        count = 1
        while meeting_node.next.val != meeting_val:
            count += 1
            meeting_node = meeting_node.next
        return count


    # 3. 找出环的入口节点
    #   - 仍旧设置两个指针，从头结点开始，一个先走n步，另一个才开始走
    #   - 两个节点第一次相遇，即为环的入口节点
    def get_entry_node(self):
        n = self.count_rings()

        slow, fast = self.head.next, self.head.next
        # 快指针先走n步
        while n:
            fast = fast.next
            n -= 1

        # 快慢同时走，直到相遇
        while slow.val != fast.val:
            slow = slow.next
            fast = fast.next

        return slow.val, slow  # 相遇的节点


def main():
    # 新建一个链表
    print("新建一个链表")
    ll = LinkedList()
    for i in range(10):
        ll.add_first(i)
    ll.print_lkst()
    ll.cread_ring_node(6)

    print('是否有环')
    print(ll.has_ring())
    print('环的节点数')
    print(ll.count_rings())
    print('查找环入口')
    print(ll.get_entry_node())

if __name__ == '__main__':
    main()
