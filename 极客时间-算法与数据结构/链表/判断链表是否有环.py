# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         判断链表是否有环.py
# Author:       wdf
# Date:         11/28/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------
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

    def has_cycle(self):



# 方法一
# 用hash表记录每次访问过的元素，如果有元素第二次出现，则说明有环



def main():
    pass


if __name__ == '__main__':
    main()