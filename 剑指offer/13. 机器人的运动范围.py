#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/22/2020 12:47 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        13. 机器人的运动范围
# description:      m行n列的方格，机器人可以走的格子的坐标的数位之和不能大于k， 问机器人可以到达多少个格子
# eg:
# 示例，k = 19， 坐标（35,37）的数位之和： 3+5+3+7=18，可以走，坐标{33,38）就不可以走

# visited[row][col] = True


def check(k, m, n, row, col, visited):
    '''检查当前位置可不可以走'''
    if 0 <= row < m and 0 <= col < n:
        total = sum(map(int, str(col) + str(row)))  # 计算数字的数位之和
        if total <= k and \
                not visited[row][col]:
            return True

    return False


def moving_count(m, n, k):
    '''
    m行 n列， 阈值为k
    :param m:
    :param n:
    :param k:
    :return:
    '''

    if k < 0 or m <= 0 or n <= 0:
        return 0

    visited = [[False for _ in range(m+1)] for _ in range(n+1)]
    count = _dfs_moving_count(k, m, n, 0, 0, visited)
    return count


def _dfs_moving_count(k, m, n, i, j, visited):
    count = 0
    if check(k, m, n, i, j, visited):
        visited[i][j] = True
        count = 1 + _dfs_moving_count(k, m, n, i - 1, j, visited) \
                + _dfs_moving_count(k, m, n, i, j - 1, visited) \
                + _dfs_moving_count(k, m, n, i + 1, j, visited) \
                + _dfs_moving_count(k, m, n, i, j + 1, visited)
    return count


def main():
    print(moving_count(3, 4, 3))


if __name__ == '__main__':
    main()
