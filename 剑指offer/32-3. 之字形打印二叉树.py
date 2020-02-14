#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/9/2020 3:42 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        32-3. 之字形打印二叉树
# description:      从左到右——从右到左打印，呈之字形
# usage:            

class Node(object):
    '''节点类 '''

    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


# 不分层
def zhi_order(root):
    # 先在纸上演示，可以知道先入后出，需要栈，且需要两个栈
    left_to_right = []  # 堆栈，先左后右
    right_to_left = []  # 堆栈，先右后左

    right_to_left.append(root)  # 根节点
    level = 0  # 当前层级

    cur_stack = right_to_left

    while cur_stack:
        node = cur_stack.pop()
        print(node.value, end=' ')

        if level % 2 == 0:  # 0、2、4、6层
            if node.lchild:
                left_to_right.append(node.lchild)
            if node.rchild:
                left_to_right.append(node.rchild)
        else:  # 1、3、5、7层
            if node.rchild:
                right_to_left.append(node.rchild)
            if node.lchild:
                right_to_left.append(node.lchild)

        # 如果当前栈不为空，说明当前层还有节点没有遍历完
        if not cur_stack:  # 为空，则考虑下一层
            level += 1
            cur_stack = right_to_left if level % 2 == 0 else left_to_right


# 分层
def zhi_order_per_layers(root):
    # 先在纸上演示，可以知道先入后出，需要栈，且需要两个栈
    left_to_right = []  # 堆栈，先左后右
    right_to_left = []  # 堆栈，先右后左

    right_to_left.append(root)  # 根节点
    level = 0  # 当前层级
    to_be_print = 1   # 当前层还未打印的节点数
    cur_level_nodes = 0  # 统计当前层的节点数
    cur_stack = right_to_left

    while cur_stack:
        node = cur_stack.pop()
        print(node.value, end=' ')

        if level % 2 == 0:  # 0、2、4、6层
            if node.lchild:
                left_to_right.append(node.lchild)
                cur_level_nodes += 1
            if node.rchild:
                left_to_right.append(node.rchild)
                cur_level_nodes += 1
        else:  # 1、3、5、7层
            if node.rchild:
                right_to_left.append(node.rchild)
                cur_level_nodes += 1
            if node.lchild:
                right_to_left.append(node.lchild)
                cur_level_nodes += 1

        # 如果当前栈不为空，说明当前层还有节点没有遍历完
        if not cur_stack:  # 为空，则考虑下一层
            level += 1
            cur_stack = right_to_left if level % 2 == 0 else left_to_right

        # 分层、换行
        to_be_print -= 1
        if to_be_print == 0:
            print()  # 换行
            to_be_print = cur_level_nodes  # 待打印的节点数（更新为下一层的节点总数）
            cur_level_nodes = 0  # 重置为0、统计下一层节点总数


def main():
    root = Node('1',
                Node('2',
                     Node('4',
                          Node('8'),
                          Node('9')),
                     Node('5',
                          Node('10'),
                          Node('11'))),
                Node('3',
                     Node('6',
                          Node('12'),
                          Node('13')),
                     Node('7',
                          Node('14'),
                          Node('15'))))
    print('之字形遍历，不分行')
    zhi_order(root)
    print()

    print('之字形遍历，分行')
    zhi_order_per_layers(root)
    print()


if __name__ == '__main__':
    main()
