# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         reduce归约函数.py
# Author:       wdf
# Date:         12/8/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

from functools import  reduce

'''reduce， 二元操作符，先把前两个元素进行运算， 得到的结果在于第三个元素进行运算……'''

lst = [1,2,3,4,5]
print(reduce(lambda x,y: x+y, lst))

# 也可以指定初始值 100
# 先把100和第一个元素相加，得到的结果再与第二个进行运算……
print(reduce(lambda x,y: x+y, lst, 100))

def main():
    pass


if __name__ == '__main__':
    main()