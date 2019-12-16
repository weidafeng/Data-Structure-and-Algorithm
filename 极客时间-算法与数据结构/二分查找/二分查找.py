# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         二分查找.py
# Author:       wdf
# Date:         12/16/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

# 非递归写法
def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (right - left) // 2 + left  # 求中间元素（也可以写为 （left+rigjht)//2
        if array[mid] == target:
            return mid

        elif array[mid] < target:  # 去右边查找
            left = mid + 1
        else:  # 去左边查找
            right = mid - 1
    return -1  # 未找到


# 递归写法(与循环写法相比，效率不高）
def binary_search_recursively(array, target, low, high):
    if high < low:
        return -1
    mid = (high - low) // 2 + low
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search_recursively(array, target, low=mid + 1, high=high)
    else:
        return binary_search_recursively(array, target, low=low, high=mid - 1)



def main():
    lst = [33,22,34,71,69, 99, 77, 70, 89, 90, 100]
    lst.sort()  # 输入的一定要是有序数组
    print(lst)
    print(binary_search(lst, 70))
    print(binary_search_recursively(lst, 70, 0, len(lst)))


if __name__ == '__main__':
    main()