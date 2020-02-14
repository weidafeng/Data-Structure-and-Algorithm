#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/21/2020 12:15 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        9. 用两个栈实现队列
# description:      实现在队列尾部插入节点，和在队列头部删除节点两个功能。
# usage:            

class Queue_with_Two_Stacks:
    def __init__(self):
        self.stack_A = []  # 入栈
        self.stack_B = []  # 出栈

    def append_tail(self,elem):
        '''在末尾插入元素'''
        # 插入元素，只从A栈插入
        self.stack_A.append(elem)
        return self

    def delete_head(self):
        '''删除第一个元素'''
        # 删除元素，只从栈B删除——如果B栈不为空，可以直接删除（因为B栈栈顶是最先放入的元素）
        # ——如果B栈为空，先把A栈的所有元素压入B栈，再从B栈弹出
        if self.stack_B:
            return self.stack_B.pop()
        else:
            while self.stack_A:
                self.stack_B.append(self.stack_A.pop())
            return self.stack_B.pop()



def main():
    queue = Queue_with_Two_Stacks()
    for i in range(5):
        queue.append_tail(i)
    print(queue.stack_A)
    print(queue.delete_head())
    print(queue.delete_head())
    print(queue.delete_head())


    queue.append_tail(7)
    queue.append_tail(8)
    print(queue.delete_head())
    print(queue.delete_head())
    print(queue.delete_head())

if __name__ == '__main__':
    main()
