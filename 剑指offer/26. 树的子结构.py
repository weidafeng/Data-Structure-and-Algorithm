#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/7/2020 12:56 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        26. 树的子结构
# description:      输入两棵二叉树AB， 判断B是不是A的子结构
# # usage:
# A树
#         8
#     8       7
# 9       2
#     4       7
# 与B树
#     8
# 9       2


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


########### 判断B是否为A的子结构 #############

# 第一步，找到根节点相同的节点
def has_sub_tree(A, B):
    result = False
    if A is not None and B is not None:
        if A.value == B.value:  # 找到相同的根节点，则往下遍历，比较子树
            result = dose_tree_a_has_tree_b(A, B)
        if not result:  # 如果没有找到，则继续往下找,看看A的左子树是否相同
            result = has_sub_tree(A.lchild, B)
        if not result:  # 看看A的右子树是否相同
            result = has_sub_tree(A.rchild, B)

    return result


# 第二步，递归调用，判断左右子树
def dose_tree_a_has_tree_b(root_a, root_b):
    if root_b is None:  # B子树为空
        return True
    if root_a is None:  # A子树为空
        return False

    if root_a.value != root_b.value:  # 如果节点的值不相同
        return False
    # 递归调用，判断他的左右子树
    return dose_tree_a_has_tree_b(root_a.lchild, root_b.lchild) and dose_tree_a_has_tree_b(root_a.rchild, root_b.rchild)


def main():
    root = Node('D',
                Node('B', Node('A'), Node('C')),
                Node('E', rchild=Node('G', Node('F'))))
    print(root)
    print('先序遍历')
    pre_order(root)
    print()
    print('中序遍历')
    in_order(root)
    print()

    root_2 = Node('D',
                Node('B', Node('A')),
                Node('E', rchild=Node('G')))
    print(root_2)
    print('先序遍历')
    pre_order(root_2)
    print()
    print('中序遍历')
    in_order(root_2)
    print()

    print(has_sub_tree(root, root_2))


if __name__ == '__main__':
    main()
