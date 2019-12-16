# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         位运算求子集.py
# Author:       wdf
# Date:         12/14/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

def get_sub_set(list_demo):
    sub_list_all = []  # 用于存放集合所有的子集
    for i in range(1 << len(list_demo)):  # 循环遍历0到2**n之间的每个数, 1 右移了 n位，即2 的n次方
        combo_list = []  # 用于存放每个单独的循环中取出的子集
        for j in range(len(list_demo)):
            if i & (1 << j):  # 每一个数用&操作判断第i位上是否有1。 1<<j ，j每次增加一，表示比较的是第j个元素
                combo_list.append(list_demo[j])  # 有的话保存起来
        sub_list_all.append(combo_list)
    return sub_list_all
'''放入的顺序：
i   i   num
0   0   空集
1   1   a
2   10  b
3   11  ab
4   100 c
5   101 ac
...

'''

def main():
    list_demo = ['a', 'b', 'c']
    sub_list_all = get_sub_set(list_demo)
    print(sub_list_all)
    print(len(sub_list_all))


if __name__ == '__main__':
    main()