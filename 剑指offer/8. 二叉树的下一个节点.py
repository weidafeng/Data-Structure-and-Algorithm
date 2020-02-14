#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/21/2020 11:24 AM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        8. 二叉树的下一个节点
# description:      给定一个二叉树和其中一个节点，找到中序遍历方式下的下一个节点
# usage:            


# 方法一，中序遍历完整个二叉树，再在结果中找到下一个元素
class Node(object):
    '''节点类 '''
    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    def __init__(self):
        self.root = Node()
        self.my_queue = []  # 存储各个节点
        self.result = []  # 中序遍历的结果

    def add(self, value):
        '''为树添加节点（完全二叉树）'''
        node = Node(value)  # 初始化一个节点
        if self.root.value == None:  # 如果树是空的，则该节点为根节点
            self.root = node
            self.my_queue.append(self.root)

        else:  # 不是空树，且该节点的左右子树还有空缺
            tree_node = self.my_queue[0]
            if tree_node.lchild == None:  # 如果左儿子没有值，则插到左儿子处
                tree_node.lchild = node
                self.my_queue.append(tree_node.lchild)

            else:  # 左儿子有值，则插到右边
                tree_node.rchild = node
                self.my_queue.append(tree_node.rchild)
                # 注意，插入右儿子后，该节点的左右子树均已满，
                # 需要丢弃该节点（方便下次插入时找准位置）
                self.my_queue.pop(0)

    def in_order(self, root):
        if root == None:
            return
        self.in_order(root.lchild)
        self.result.append(root.value)
        # print(root.value, end=' ')
        self.in_order(root.rchild)
    
    def find_next(self, value):
        return self.result[self.result.index(value) + 1]



### 剑指offer方法
#### 方法二，利用二叉树中序遍历的特性

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def get_next(self, node):
        if node is None:
            return
        parent = None
        if node.right: # 存在右子树，则右子树最左子树就是下一个节点
            node = node.right
            while node.left:
                node = node.left
            next = node

        else:  # 不存在右子树
            if  node.parent and node.parent.left == node:  # 如果当前节点是他父亲节点的左子节点，那下一个节点就是他的父亲节点
                next = node.parent
            elif node.parent and node.parent.right == node:   #当前节点是他父亲节点的右子节点，情况比较复杂，可以沿着父节点一直向上回溯，直到找到一个节点，该节点是他父亲节点的左子节点
                node = node.parent
                while node.parent and node.parent.right == node:
                    node = node.parent
                # 遍历终止时，还有父节点，说明当前节点是父节点的左子节点，则中序遍历的下一个节点为当前节点的父亲节点
                if node.parent:
                    next = node.parent
                # 如果没有父节点，说明没有下一个了，直接返回None（上面定义过了，next = None）

        return next





def main():
    tree = BinaryTree()
    elems = range(10)
    for elem in elems:
        tree.add(elem)

    print(tree.in_order(tree.root))
    print(tree.result)
    print(tree.find_next(9))


if __name__ == '__main__':
    main()
