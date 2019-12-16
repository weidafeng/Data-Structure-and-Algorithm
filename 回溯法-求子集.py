# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         回溯法-求子集.py
# Author:       wdf
# Date:         2019/9/13
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

# 使用回溯法解决子集问题

def subset_recursive(nums):
    lst = []
    result = []  # 最终返回的结果，会把lst[]一个一个放到result[]里
    subset_recursive_helper(result, lst, nums, 0)
    return result


def subset_recursive_helper(result, lst, nums, position):
    result.append(lst[:])  # 先把上次的结果加进去，注意，这是加进去的是个copy
    print(lst[:])  # 每次被放进去的东西
    for i in range(position, len(nums)):  # 考虑数组里还没有被放进去的元素
        lst.append(nums[i])  # 每次放入一个元素
        subset_recursive_helper(result, lst, nums, i + 1)
        lst.pop()  # 恢复上次访问时的状态，开始回溯



def main():
    subset_recursive(['a', 'b', 'c'])


if __name__ == '__main__':
    main()