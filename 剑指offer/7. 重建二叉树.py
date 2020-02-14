#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/21/2020 9:23 AM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        7. 重建二叉树
# description:      根据二叉树的前序遍历、中序遍历的结果，重建二叉树。 二叉树中没有重复元素。
# usage:            


# 思路：
# 前序遍历： 根 左 右
# 中序遍历： 左 根 右

# 前序遍历的第一个节点一定是根节点，因为没有重复的元素，所以可以在中序遍历的结果中找到根节点
# 中序遍历根节点左边都是左子树（假如有x个节点），右边都是右子树
# 前序遍历根节点后面的x节点都是左子树，剩下的元素都是右子树

# 同样的方法，可以在根节点的左子树中，从前序遍历的结果找到根节点，再利用这个值从中序遍历的结果找到左右子树的元素个数，再返回前序遍历的结果中确定位置

# 整个思想是递归实现

# 二叉树节点
class BinaryTreeNode():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def construct_binary_tree(pre_order, in_order):
    '''
    重建二叉树
    :param pre_order: 前序遍历的结果
    :param in_order:  中序遍历的结果
    :return:
    '''
    if not pre_order and not in_order:
        return None
    if set(pre_order) != set(in_order):  # 异常情况，两种遍历结果不一致，出错了
        return None
    root = BinaryTreeNode(pre_order[0])  # 整个二叉树的根节点
    root_index = in_order.index(pre_order[0])  # 找到根节点在中序遍历中的索引（也即左子树的元素的个数）

    # 递归构建左子树
    root.left = construct_binary_tree(pre_order[1:root_index + 1], in_order[:root_index])
    # 递归构建右子树
    root.right = construct_binary_tree(pre_order[root_index + 1:], in_order[root_index + 1:])

    return root


def main():
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    in_order = [4, 7, 2, 1, 5, 3, 8, 6]
    tree = construct_binary_tree(pre_order,in_order)
    print(tree)  # 可以debug看二叉树的结构

if __name__ == '__main__':
    main()
