#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/22/2020 11:09 AM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        12. 矩阵中的路径-回溯法
# description:      判断一个二维矩阵中是否存在指定路径
# 示例:
# lst = [
#     ['a', 'b', 't', 'g'],
#     ['c', 'g', 'c', 's'],
#     ['j', 'd', 'e', 'h']
# ]
#
# path = 'bfce' -> 存在
# path = 'abfb' -> 不存在

def string_path_in_matrix(lst, path):
    '''
    回溯法，一般可以用递归实现，用栈存储路径。同时需要一个visited_set，记录已经访问过的路径（不能重复使用）
    方向： 右、下、左、上
    :param lst:  矩阵
    :param path:  待查找路径
    :return:  true or false
    '''

    if not len(lst) or not len(lst[0]):
        return None
    if not path:
        return None

    visited_set = [[False for _ in range(len(lst))] for _ in range(len(lst[0]))]

    path_idx = 0
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            # 从第一个元素开始，沿着该元素的四个方向遍历
            if _dfs_has_path(lst, i, j, visited_set, path_idx, path):
                return True
            # 不行的话就从下一个元素开始遍历
    # 没有可行解
    return False


def _dfs_has_path(lst, row, col, visited_set, path_idx, path):
    '''
    递归搜索
    :param lst: 矩阵
    :param row: 当前位置
    :param col: 当前位置
    :param visited_set:  访问标识
    :param path_idx:  正在找的路径元素索引
    :param path:  路径
    :return:
    '''

    # 终止标志， 已经找到最后一个元素
    if path_idx == len(path):
        return True

    has_path = False  # 默认为false，表示还没有找到路径

    # 当前位置不越界、是要找的元素、之前没有访问过
    if 0 <= row < len(lst) and 0 <= col < len(lst[0]) and lst[row][col] == path[path_idx] and not visited_set[row][col]:
        path_idx += 1  # 找到一个
        visited_set[row][col] = True  # 已经访问过了

        # 递归， 在当前元素的四个方向上找下一个元素
        has_path = _dfs_has_path(lst, row - 1, col, visited_set, path_idx, path) \
                   or _dfs_has_path(lst, row, col - 1, visited_set, path_idx, path) \
                   or _dfs_has_path(lst, row + 1, col, visited_set, path_idx, path) \
                   or _dfs_has_path(lst, row, col + 1, visited_set, path_idx, path)

        if not has_path:  # 当前结果不行（没有走到最后一层，即此路不通），回溯、复原当前状态
            path_idx -= 1
            visited_set[row][col] = False

    # 除非沿着某条路径走到了最后一层，才会返回True
    return has_path  # 返回最终结果


def main():
    lst = [
        ['a', 'b', 't', 'g'],
        ['c', 'g', 'c', 's'],
        ['j', 'd', 'e', 'h']
    ]

    path1 = 'bgce'
    path2 = 'abfb'
    print(string_path_in_matrix(lst, path1))
    print(string_path_in_matrix(lst, path2))
    print(string_path_in_matrix(lst, 'btcgcj'))


if __name__ == '__main__':
    main()
