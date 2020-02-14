#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/9/2020 4:28 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        33. 二叉搜索树的后序遍历
# description:      给定一个数组，判断该数组是否为某二叉搜索树的后序遍历结果
# usage:            二叉搜索树的左子树都比根节点小，右子树都比根节点大； 假设数的所有元素都不相同
# eg 
# [5,7,6,9,11,10,8] 是下面这个二叉搜索树的后序遍历
#             8
#     6               10
# 5       7       9       11


def verify_binary_search_tree(lst):
    '''
    给定一个数组，判断他是否为某二叉搜索树的后序遍历结果
    
    思路：
    后序遍历的结果中，最后一个元素是根节点
    依据二叉搜索树的性质，左子树都小于根节点的值、右子树都大于根节点，可以根据根节点的大小，把数组分成左右两部分
    然后递归比较左右部分
    '''
    # 递归终止条件
    if len(lst) <= 2:
        return True

    root = lst[-1]  # 最后一个元素是根节点
    # 找到第一个大于根节点的元素索引
    cut_index = 0  # 表示划分左右子树的点的索引
    for i in range(len(lst)):
        if lst[i] > root:
            break
        cut_index += 1

    # 判断右子树是否有小于根节点的元素——如果有，则错误
    for j in range(cut_index + 1, len(lst)):
        if lst[j] < root:
            return False

    # 递归遍历，分别判断左右子树
    if cut_index > 0:  # 注意这个条件，没有左子树或者右子树
        return verify_binary_search_tree(lst[:cut_index]) and verify_binary_search_tree(lst[cut_index:])
    return True


def main():
    lst = [5]
    print(verify_binary_search_tree(lst))
    lst = [5, 7, 6, 9, 11, 10, 8]
    print(verify_binary_search_tree(lst))
    lst = [7, 4, 6, 5]
    print(verify_binary_search_tree(lst))


if __name__ == '__main__':
    main()
