#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/7/2020 2:06 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        28. 对称的二叉树
# description:      判断给定的二叉树是否是对称的，所谓对称是指，一个二叉树和他的镜像一样
# usage:            

class Node(object):
    '''节点类 '''

    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


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


####### 对称的二叉树  ########
# 方法一， 镜像后，比较遍历的结果是否一致

### 先序遍历 测试用 ####
def pre_order(root, result):
    if root is None:
        return
    result.append(root.value)
    pre_order(root.lchild, result)
    pre_order(root.rchild, result)


def is_symmetrical(root):
    # 存储原始二叉树的先序遍历结果
    result_raw = []
    pre_order(root, result_raw)

    # 求镜像二叉树
    mirror_tree(root)
    # 存储镜像二叉树的先序遍历结果
    result_mirror = []
    pre_order(root, result_mirror)

    print('原始：{} '.format(result_raw))
    print('镜像：{} '.format(result_mirror))
    return result_mirror == result_raw


####### 对称的二叉树  ########
# 方法二，定义一个新的遍历方法
# 传统先序遍历是： 根左右
# 对称先序遍历是： 根右左  —— 对称

# 如果二叉树是对称的，那么两种遍历方法的结果应该一致
def is_symmetrical_2(root):
    return is_symmetrical_2_helper(root, root)

# 辅助函数
def is_symmetrical_2_helper(left, right):
    # 如果左右子树都为空，则对称
    if left is None and right is None:
        return True
    # 如果一棵树为空、另一个不为空，则不对称
    elif left is None or right is None:
        return False

    # 两个子树都不为空， 但不对称
    if left.value != right.value:
        return False

    # 递归调用，比较左子树的左节点和右子树的右节点、左子树的右节点和右子树的左节点
    return is_symmetrical_2_helper(left.lchild, right.rchild) and is_symmetrical_2_helper(left.rchild, right.lchild)



def main():
    root = Node('D',
                Node('B', Node('A'), Node('C')),
                Node('E', rchild=Node('G', Node('F'))))

    print(is_symmetrical(root))
    print(is_symmetrical_2(root))
    root = Node('D',
                Node('B', Node('A'), Node('C')),
                Node('B', Node('C'), Node('A')))

    print(is_symmetrical(root))
    print(is_symmetrical_2(root))


if __name__ == '__main__':
    main()
