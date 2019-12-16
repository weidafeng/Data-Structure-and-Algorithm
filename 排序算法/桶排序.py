# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         桶排序.py
# Author:       wdf
# Date:         11/28/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  每一个桶（bucket） 代表一个区间范围， 里面可以承载一个或多个元素。
# Usage：
#-------------------------------------------------------------------------------

# 第1步，创建桶，并确定每一个桶的区间范围。
#   具体需要建立多少个桶， 如何确定桶的区间范围， 有很多种不同的方
#   式。 我们这里创建的桶数量等于原始数列的元素数量， 除最后一个桶只
#   包含数列最大值外， 前面各个桶的区间按照比例来确定。
#
#   区间跨度 = （最大值-最小值） / （桶的数量 - 1）
#
# 第2步， 遍历原始数列， 把元素对号入座放入各个桶中。
# 第3步， 对每个桶内部的元素分别进行排序（显然， 只有第1个桶需要排序） 。
# 第4步， 遍历所有的桶， 输出所有元素。

def bucket_sort(lst, n_bucket=5):
    largest, smallest = max(lst), min(lst)
    span = (largest - smallest) // n_bucket
    bucket = [ [] for _ in range(n_bucket+1)]
    print(span, bucket)
    # 第二步，遍历原始数列、放入桶中
    for item in lst:
        idx = (item - smallest) // span
        bucket[idx].append(item)

    # 第三步，对各个桶的元素进行排序
    for i in bucket:
        i.sort()

    # 第四步，遍历桶，输出元素
    sorted_list = []
    print(bucket)
    for i in range(n_bucket + 1):
        # if bucket[i] != 0:
        sorted_list += bucket[i]

    return sorted_list


def main():
    lst = [4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10]
    print(lst)
    print(bucket_sort(lst,5))


if __name__ == '__main__':
    main()