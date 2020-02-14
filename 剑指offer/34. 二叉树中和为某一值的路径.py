#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/9/2020 4:56 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        34. 二叉树中和为某一值的路径
# description:      输入一棵二叉树和一个整数，打印出二叉树中节点值的和为该整数的所有路径（从根节点到叶节点为一条路径）
# usage:            

# 先序遍历，根左右

class Node(object):
    '''节点类 '''

    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


# 使用堆栈实现先序遍历
def find_path(root, total):
    if root is None:
        return
    path = []  # 堆栈存储路径
    cur_sum = 0
    find_path_helper(root, path, cur_sum, total)


def find_path_helper(root, path, cur_sum, total):
    cur_sum += int(root.value)  # 和累加
    path.append(root.value)     # 记录路径

    if root.lchild is None and root.rchild is None:  # 如果是叶节点
        if cur_sum == total:  # 找到一条路径
            print(path)
    else:        # 如果不是叶节点，则往下遍历
        if root.lchild:
            find_path_helper(root.lchild, path, cur_sum, total)
        if root.rchild:
            find_path_helper(root.rchild, path, cur_sum, total)

    # 不是叶节点，或叶节点不符合条件——回溯
    # 在返回父节点之前，删除当前节点
    path.pop()


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
    total = 22
    find_path(root, total)

    root = Node('10',
                Node('5',
                     Node('4'),
                     Node('7')),
                Node('12'))
    total = 22
    find_path(root, total)


if __name__ == '__main__':
    main()
