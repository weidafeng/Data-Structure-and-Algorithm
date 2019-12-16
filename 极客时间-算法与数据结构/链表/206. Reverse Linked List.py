# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         206. Reverse Linked List.py
# Author:       wdf
# Date:         11/5/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

class ListNode:
    def __init__(self,x):
        self.val = x
        self.node = None

class Solution:
    def reverse_list(self, head):
        '''
        reverse a linked list
        :param head: linked node
        :return: linked node
        '''
        cur, pre = head, None
        while cur.next != None:
            cur.next = pre # 指向前一个节点（反转）
            pre = cur # 向后移，准备处理下一个
            cur = cur.next # 向后移，准备处理下一个
        return cur


if __name__ == '__main__':
    pass