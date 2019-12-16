# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         全排列.py
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
def perms(elements):
    if len(elements) <= 1:  # base，如果只有一个元素，直接输出
        yield elements
    else:
        for perm in perms(elements[1:]): # 每次减去第一个元素，直到只剩最后一个元素
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def main():
    for item in list(perms([1, 2, 3])):
        print(item)


if __name__ == '__main__':
    main()