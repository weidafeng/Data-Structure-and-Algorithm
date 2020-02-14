#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/18/2020 10:18 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        3. 数组中重复的数字
# description:      长度为n的数组，所有数字都在0-n-1大小范围内，某些数字是重复的，但不知道重复了几个数字，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
# example：          input： 长度n=7， 数组lst=[2,3,1,0,2,5,3]，
#                   output： 2或者3
# usage:            

def find_duplicate(lst, n):
    '''
    找到任意一个重复的数字
    方法一： set计数，当出现次数多余一次，则直接返回
    复杂度： 时间O(n）， 空间O（n）
    :param lst: 
    :param n:   数组长度，且每个元素都小于n
    :return: 
    '''
    count = {}
    for i in lst:
        count.setdefault(i, 0)
        count[i] += 1
        if count[i] >= 2:
            return i


def find_duplicate_2(lst, n):
    '''
    找到任意一个重复的数字
    方法二： 先排序，再从头到尾逐个元素比较是否重复
    复杂度： O(nlogn)
    :param lst: 
    :param n:   数组长度，且每个元素都小于n
    :return: 
    '''
    lst.sort()
    for i in range(n - 1):
        if lst[i] == lst[i + 1]:
            return lst[i]


def find_duplicate_3(lst, n):
    '''
    找到任意一个重复的数字
    方法三： 利用题目的特殊性：每个数字都小于n，那么一个萝卜一个坑，从头开始，把每个萝卜放到每个坑里
    复杂度： 时间O(n)，空间O(1)
    :param lst: 
    :param n:   数组长度，且每个元素都小于n
    :return: 
    '''
    i = 0
    while i < n:
        if lst[i] == i:  # 一个萝卜一个坑，没有站错位置
            i += 1
        elif lst[i] == lst[lst[i]]:  # 站错位置了，且应该放的正确的位置已经占了，说明重复
            return lst[i]
        else:  # 站错位置了，交换，摆正（这个摆正只能保证当前元素放到合适的位置，不能保证交换过来的元素位置正确）
            # 注意这个交换，要指定中间变量，因为中间会直接修改数组
            tmp = lst[i]
            lst[i] = lst[lst[i]]
            lst[tmp] = tmp

        print(lst)


def main():
    lst = [2, 3, 1, 0, 2, 5, 3]
    n = len(lst)

    print(find_duplicate(lst, n))

    lst = [2, 3, 1, 0, 2, 5, 3]
    n = len(lst)
    print(find_duplicate_2(lst, n))

    lst = [2, 3, 1, 0, 2, 5, 3]
    n = len(lst)
    print(find_duplicate_3(lst, n))


if __name__ == '__main__':
    main()
