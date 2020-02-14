#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/9/2020 1:23 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        32. 从上到下打印二叉树（不分行）
# description:      层序遍历、不分行
# usage:            

# 队列实现层序遍历

class Node(object):
    '''节点类 '''
    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


def layer_order(root):
    # 层序遍历，不分行，队列实现
    if root is None:
        return

    queue = [root]  # python 可以用列表实现queue

    while queue:
        node = queue.pop(0)
        print(node.value, end=' ')

        # 每访问一个节点，都先把他的左右子节点放进队列
        if node.lchild is not None:
            queue.append(node.lchild)
        if node.rchild is not None:
            queue.append(node.rchild)



def main():
    root = Node('D',
                Node('B', Node('A'), Node('C')),
                Node('E', rchild=Node('G', Node('F'))))
    print('层序遍历，不分行', end=' ')
    layer_order(root)
    print()

    root = Node('D',
                Node('B', Node('A')),
                Node('E', rchild=Node('G')))
    print('层序遍历，不分行', end=' ')
    layer_order(root)

if __name__ == '__main__':
    main()
