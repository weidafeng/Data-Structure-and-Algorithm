#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/9/2020 12:19 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        30. 包含min函数的栈
# description:      定义栈的数据结构，实现min函数，要求min、push、pop的时间复杂度均为0（1）
# usage:            

# 实现思路： 用两个栈，一个栈正常存储数据，另一个栈存储当前最小值

class MinStack():
    def __init__(self):
        self.val_stack = []  # 数据栈
        self.min_stack = []  # 辅助栈，存储当前最小值

    def push(self, val):
        '''入栈'''
        self.val_stack.append(val)
        if len(self.min_stack) == 0:  # 如果是第一个元素，则直接入栈
            self.min_stack.append(val)
        else:
            # 比较、存储当前最小值
            cur_min = self.min_stack[-1] if self.min_stack[-1] <= val else val
            self.min_stack.append(cur_min)

    def pop(self):
        '''出栈'''
        if len(self.val_stack):  # 只需要判断栈内是否还有元素
            res = self.val_stack.pop()
            self.min_stack.pop()
            return res
        else:
            return None

    def min(self):
        '''找到最小值'''
        return self.min_stack[-1]


def main():
    stack = MinStack()

    lst = [3, 4, 2, 1]
    for val in lst:
        stack.push(val)
        print(stack.val_stack)
        print(stack.min_stack)
        print(stack.min())

    stack.pop()
    print(stack.val_stack)
    print(stack.min_stack)
    print(stack.min())

    stack.pop()
    print(stack.val_stack)
    print(stack.min_stack)
    print(stack.min())

    stack.push(0)
    print(stack.val_stack)
    print(stack.min_stack)
    print(stack.min())


if __name__ == '__main__':
    main()
