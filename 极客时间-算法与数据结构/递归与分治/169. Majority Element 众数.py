# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         169. Majority Element 众数.py
# Author:       wdf
# Date:         12/10/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------


# 169. Majority Element
# 出现次数大于 n/2

# 方法一 构建一个hash set，记录每个元素出现的次数，返回出现次数最多的元素
# Runtime: 176 ms, faster than 91.55% of Python3 online submissions for Majority Element.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Majority Element.
def majority(nums):
    count_set = {}
    for x in nums:
        if x in count_set:
            count_set[x] += 1
        else:
            count_set[x] = 1
    return max(count_set.items(),key=lambda kv:kv[1])[0]

# 代码精简（虽然代码量少了，但时间复杂度更高）
# list。count() 是 O(N)
# 生成式也是O(N)
# 总的复杂度为O(N^2)
# 超时
def majority2(nums):
    count_set = {num:nums.count(num) for num in nums}
    # print(count_set)
    return max(count_set.items(),key=lambda kv:kv[1])[0]


# 取巧： 因为题目限定众数出现次数 > n/2，且一定有解
# 则先排序，中间的元素一定是
# O(nlog(n))
# Runtime: 172 ms, faster than 95.65% of Python3 online submissions for Majority Element.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Majority Element.
def majority3(nums):
    nums.sort()
    return nums[len(nums)//2]

def main():
    lst = [2,2,1,1,1,2,2]
    print(majority(lst))
    print(majority2(lst))
    print(majority3(lst))

if __name__ == '__main__':
    main()