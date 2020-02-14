#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/7/2020 1:50 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        27. 二叉树的镜像
# description:      输入一个二叉树，输出他的镜像
# usage:            


class Node(object):
    '''节点类 '''
    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


### 先序遍历 测试用 ####
def pre_order(root):
    if root is None:
        return
    print(root.value, end='  ')
    pre_order(root.lchild)
    pre_order(root.rchild)


### 中序遍历 测试用 ####
def in_order(root):
    if root is None:
        return
    in_order(root.lchild)
    print(root.value, end='  ')
    in_order(root.rchild)


######  镜像二叉树  ########
def mirror_tree(root):
    # 同样递归实现，交换左右子树
    if root is None:
        return
    if root.lchild is None and root.rchild is None:  # 左右子树均为空，返回（已经遍历到最后一层）
        return

    # 交换左右子树 (即便有其中一个节点没有子树，也交换（是None))
    root.lchild, root.rchild = root.rchild, root.lchild

    # 递归调用，处理左右子树
    if root.lchild:
        mirror_tree(root.lchild)
    if root.rchild:
        mirror_tree(root.rchild)


def main():
    root = Node('D',
                Node('B', Node('A'), Node('C')),
                Node('E', rchild=Node('G', Node('F'))))
    print('**********交换前***********')
    print('先序遍历', end=' ')
    pre_order(root)
    print()
    print('中序遍历', end=' ')
    in_order(root)
    print()
    print('**********交换后***********')
    mirror_tree(root)
    print('先序遍历', end=' ')
    pre_order(root)
    print()
    print('中序遍历', end=' ')
    in_order(root)
    print()

    print('*' * 25)

    root = Node('D',
                Node('B', Node('A')),
                Node('E', rchild=Node('G')))
    print('**********交换前***********')
    print('先序遍历', end=' ')
    pre_order(root)
    print()
    print('中序遍历', end=' ')
    in_order(root)
    print()
    print('**********交换后***********')
    mirror_tree(root)
    print('先序遍历', end=' ')
    pre_order(root)
    print()
    print('中序遍历', end=' ')
    in_order(root)
    print()


if __name__ == '__main__':
    main()
