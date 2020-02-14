#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/18/2020 10:18 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        3. 数组中重复的数字，不允许修改原数组
# description:      长度为n+1的数组，所有数字都在1-n大小范围内，至少有一个数字重复，找出重复的数字，且不能修改原数组
# example：          input： 长度n=8， 数组lst=[2,3,5,4,3,2,6,7]，
#                   output： 2或者3
# usage:            

# 原来的两个方法都还可以用，hash set或排序
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


# 刚才的方法三不能用了，因为不能修改原数组
# 但可以构建一个辅助数组（复制一遍、在辅助数组里查找）

# 本例使用另一种思路——方法来自剑指offer
# 因为1-n区间一共只有n个数字，但给的数组里用n+1个元素——一定至少有一个重复元素
#
# 辅助函数： 计算start - end 区间内的元素一共出现了几次
def count_range(lst, start, end):
    count = 0
    for i in lst:
        if start <= i <= end:
            count += 1
    return count


def find_duplicate_3(lst, n):
    mid = n // 2
    start, end = 0, n
    while start <= end:
        mid = (end - start) // 2 + start
        count = count_range(lst, start, mid)

        # 终止条件（ 最后只剩2个元素）
        if start == end:
            if count > 1:
                return start
            else:
                break

        # 二分查找的形式
        if count > (mid - start ):
            end = mid
        else:
            start = mid + 1


def main():
    lst = [2, 3, 5, 4, 3, 2, 6, 7]
    n = len(lst)

    print(find_duplicate(lst, n))

    lst = [2, 3, 5, 4, 3, 2, 6, 7]
    n = len(lst)
    print(find_duplicate_2(lst, n))

    lst = [2, 3, 5, 4, 3, 2, 6, 7]
    n = len(lst)
    # 数组长度为8， 元素范围1-7

    print(find_duplicate_3(lst, n))


if __name__ == '__main__':
    main()
