#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/9/2020 12:36 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        31. 栈的压入、弹出序列
# description:      给出两个整数序列，第一个序列表示栈的压入顺序，判断第二个序列是否表示该栈的弹出顺序
# usage:            
# 如 12345是某栈的压入顺序， 45321是该栈对应的一个弹出顺序， 但43512就不是（43521是）


# 出栈之前必须先入栈
def is_pop_order(lst_1, lst_2):
    # 边界条件，如果两个数字个数不一样，一定不对
    if len(lst_2) != len(lst_2):
        return False
    # 如果都只有0个或1个元素
    if len(lst_1) <= 1 and len(lst_2) <= 0:
        return lst_1 == lst_2

    stack = []  # 辅助栈， 把第一个序列中的数字依次压入栈中，并按照第二个序列的顺序弹出
    i = 0  # 遍历整数序列1
    j = 0  # 表示整数序列2有多少个元素已经符合顺序了（而未采用与stack同时弹出的方法）

    while i < len(lst_1):
        while len(stack) == 0 or stack[-1] != lst_2[j]:
            stack.append(lst_1[i])
            i += 1
        # stack[-1] == lst_2[0]  相等了
        while True:
            if stack and stack[-1] == lst_2[j]:  # 如果辅助栈内还有元素，且匹配，则一直弹出
                j += 1  # 匹配数加一
                stack.pop()
                # lst_2.pop(0)   # 注意，一个是从后面弹出(stack)，一个从前面弹出（lst_2)
            else:
                break

    # 此时整数序列1的元素已经全部入栈，
    # 如果辅助栈里还有元素，则逐个比较剩下的元素是否符合整数序列2的顺序
    # 如果栈内没有元素了，此时j一定等于数字序列2的长度，不用再判断，可以直接返回True
    print(stack)
    if stack:
        for i in range(len(stack)):
            if stack.pop() != lst_2[j:].pop(0):
                return False
    return True


def main():
    lst_1 = [1, 2, 3, 4, 5]
    lst_2 = [4, 5, 3, 2, 1]  # true
    lst_3 = [4, 3, 5, 1, 2]  # false
    lst_4 = [4, 3, 5, 2, 1]  # true

    print(is_pop_order(lst_1, lst_2))
    print(is_pop_order(lst_1, lst_3))
    print(is_pop_order(lst_1, lst_4))


if __name__ == '__main__':
    main()
