#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/20/2020 8:40 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        4. 二维数组的查找
# description:      二维数组，每一行从左到右递增，每一列从上到下递增，查找一个数字是否存在在这个二维数组中
# usage:            


def find_in_matrix(lst, target):
    '''
    # 方法一，从左上角开始，依次遍历。
    利用该数组的特性： 右边和下边的所有数字都比当前数字大

    每次排除只能排除本行后面的部分元素

    :param lst: 二维数组
    :param target:  待查找的数字
    :return:  true or false
    '''

    # 边界条件 数组为空
    if not lst or not lst[0]:
        return False

    # 行遍历
    for i in range(len(lst)):
        # 列遍历
        for j in range(len(lst[0])):
            print(lst[i][j], end=' ')
            if lst[i][j] == target:  # 找到目标
                return True
            elif lst[i][j] > target:  # 比目标更大，则结束本行的遍历，跳转到下一行
                break
            else:  # 比目标更小，继续遍历
                continue
    return False


def find_in_matrix_2(lst, target):
    '''
    # 方法二，从右上角开始，依次遍历。
    **真正**利用该数组的特性： 右边和下边的所有数字都比当前数字大

    每次可以整列、整行地排除，效率更高

    :param lst: 二维数组
    :param target:  待查找的数字
    :return:  true or false
    '''

    # 边界条件 数组为空
    if not lst or not lst[0]:
        return False

    i, j = 0, len(lst[0]) - 1
    # 行遍历（从右上角、倒序）
    # 列遍历（倒序）
    while j >= 0 and i <= len(lst) - 1:
        print(lst[i][j], end=' ')
        if lst[i][j] == target:  # 找到目标
            return True
        elif lst[i][j] > target:  # 比目标更大,这一列下面的所有元素一定比目标大——这一列全部排除
            j -= 1
        else:  # 比目标更小，当前行全部都比目标小——排除整行
            i += 1
    return False


def main():
    lst = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]
    target = 70

    print(find_in_matrix(lst, target))
    print(find_in_matrix_2(lst, target))


if __name__ == '__main__':
    main()
