#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/9/2020 5:39 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        39. 数组中出现次数超过一半的数字
# description:      数组中有一个数字出现的次数超过总长度的一半，找出这个数
# usage:            
# lst = [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 总长度为9,
# 2出现了5次

# 方法一 排序、取中间的元素
# 方法二 hash set计数
def find_more_than_half(lst):
    from collections import Counter
    count = Counter()
    for c in lst:
        count.update(str(c))

    for k, v in count.items():
        if v > len(lst) // 2:
            return k


# 方法三，比较新奇
# 从前往后遍历，如果下一个数字与当前数字相同，则count+1， 否则-1,
# 因为有个数字出现的次数比其他所有数字出现的次数都多
# 所以到最后count 一定大于等于1
def find_more_than_half_2(lst):
    if not lst:
        return None

    res = lst[0]  # 初试化， 假定第一个数字
    count = 0  #
    for val in lst:
        if count == 0:  # 如果前面正负相抵了，则指定当前数字为结果、继续遍历
            res = val
            count += 1
        else:
            if val == res:  # 相同则加
                count += 1
            else:  # 不同则减
                count -= 1
    return res, count


def main():
    lst = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(find_more_than_half(lst))
    print(find_more_than_half_2(lst))


if __name__ == '__main__':
    main()
