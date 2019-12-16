# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         python手动实现链表.py
# Author:       wdf
# Date:         11/19/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
# -------------------------------------------------------------------------------

# 节点
class Node(object):
    def __init__(self, data=None, p=None):
        self.data = data
        self.next = p


# 链表
class LinkedList(object):
    def __init__(self):  # 初始化时只有一个头结点
        self.head = Node()
        self.length = 0
        print(self.head)

    # 判断链表是否为空
    def is_empty(self):
        return self.head.next == None

    # 插入元素，头插法，每次插入到最前面
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1

    def add_last(self, data):
        new_node = Node(data)
        head_node = self.head  # 保存头结点(不能直接用头结点遍历，不然会丢失整个链表）
        while head_node.next != None:  # 遍历到最后一个节点
            head_node = head_node.next
        new_node.next = head_node.next  # (即None）
        head_node.next = new_node
        self.length += 1

    def add(self, index, val):
        # 在指定位置插入节点
        if self.length >= index and index >= 0:  # 插入位置合法
            head_node = self.head
            new_node = Node(val)
            for i in range(index):
                head_node = head_node.next
            new_node.next = head_node.next
            head_node.next = new_node
            self.length += 1
        else:
            print("插入位置非法")
            return False

    def remove_first(self):
        # 删除第一个节点
        # 判断是否存在第一个节点
        # if self.head.next.next:
        if self.length > 0:
            self.head.next = self.head.next.next
            self.length -= 1
        else:
            raise ValueError('只有一个头结点')

    def remove_last(self):
        head_node = self.head
        while head_node.next.next != None:  # 找到倒数第二个节点
            head_node = head_node.next

        # 把倒数第二个节点指向None
        head_node.next = None
        self.length -= 1

    def remove(self, target):
        # 删除链表里的指定节点（默认删除找到的第一个）
        head_node = self.head
        while head_node.next:  # 还有后继节点
            if head_node.next.data == target:  # 找到目标（下一个节点）
                head_node.next = head_node.next.next  # 删除（跨过去）
                self.length -= 1
                return True
            else:
                head_node = head_node.next
        print("没有找到该节点")
        return False

    # 链表逆序
    # TODO
    def reverse(self):
        # node = self.head
        # while node.next != None: # 找到最后一个节点
        #     node = node.next
        # p, q = None, self.head
        # while q != None:
        #     tmp = q.next
        #     q.next = p
        #     p = q
        #     q = tmp
        # self.head = p
        cur, pre = self.head, None
        while cur.next != None:
            cur.next = pre # 指向前一个节点（反转）
            pre = cur # 向后移，准备处理下一个
            cur = cur.next # 向后移，准备处理下一个
        return cur


    # 打印链表
    def print_lkst(self):
        node = self.head.next  # 不打印头结点
        # print("head: ",head_node, head_node.data)
        while node != None:
            print(node.data, end=' ')
            node = node.next
        print()


def main():
    print('测试node：')
    node = Node(10)
    print(node)
    print(node.data)
    print(node.next)
    print()

    print("测试linked list： ")
    lkst = LinkedList()
    print(lkst)  # linked list
    print(lkst.head)  # node
    print(lkst.is_empty())
    print()

    # 开始添加元素
    print("开始添加元素(first)")
    lkst.add_first(10)
    print(lkst.is_empty(), lkst.length)  # False
    lkst.print_lkst()
    lkst.add_first(20)
    print(lkst.is_empty(), lkst.length)  # False
    lkst.print_lkst()
    print()

    print("开始添加元素(last)")
    lkst.add_last(30)
    lkst.add_last(40)
    lkst.print_lkst()
    print()

    print("在指定位置插入节点")
    lkst.add(3, 50)
    lkst.print_lkst()

    print()
    print()
    print("删除第一个节点")
    lkst.remove_first()
    lkst.print_lkst()

    print()
    print("删除最后一个节点")
    lkst.remove_last()
    lkst.print_lkst()

    print()
    print("删除指定元素")
    print(lkst.remove(10))
    lkst.print_lkst()
    print(lkst.remove(10))
    lkst.print_lkst()


    # 新建一个链表
    print("新建一个链表")
    ll = LinkedList()
    for i in range(10):
        ll.add_last(i)
    ll.print_lkst()

    # 逆序
    print('逆序')
    ll.reverse()
    ll.print_lkst()

    for i in range(10):
        ll.add_first(i)
    ll.print_lkst()

if __name__ == '__main__':
    main()
