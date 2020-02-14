#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 数组中数值和下标相等的元素
# 假设一个单调递增的数组中,每个元素都是整数,且唯一
# 找出数组中任意一个数值等于其下标的元素
# 如:
# lst = [-3, -1, 1, 3, 5]
# return 3

# 方法一,直接遍历

# 方法二, 利用数组有序的特性
# 二分查找
# 如果下标与值相等-- 直接输出
# 如果下标更大-- 往右半边找
# 如果值更大--  往左半边找

def get_digit_same_with_index(lst):

    if not lst:
        return None

    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        # print(mid, lst[mid])
        if lst[mid] == mid:
            return mid
        elif lst[mid] < mid:  # 下标更大,则下标与值相等的情况只可能出现在右边
            start = mid + 1
        else:
            end = mid - 1

    # 没有找到
    return None

def main():
    lst = [-3, -1, 1, 3, 5]
    print(get_digit_same_with_index(lst))


if __name__ == '__main__':
    main()