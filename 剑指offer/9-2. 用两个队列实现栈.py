#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/21/2020 12:47 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        9-2. 用两个队列实现栈
# description:      入栈、出栈操作（后入先出）
# usage:            

class Stack_with_Two_Queue:
    def __init__(self):
        import queue
        self.queue_A = queue.deque()  # 可以用列表表示队列
        self.queue_B = queue.deque()

    def delete_tail(self):
        # 删除队尾元素
        # 借助空的那个队列
        # 先让有元素的队列出队、都放到另一个队列里，最后一个元素（队尾）弹出
        if self.queue_A:
            while len(self.queue_A) > 1:
                self.queue_B.append(self.queue_A.popleft())
            return self.queue_A.popleft()
        elif self.queue_B:
            while len(self.queue_B) > 1:
                self.queue_A.append(self.queue_B.popleft())
            return self.queue_B.popleft()
        else:  # 空队列
            return None


    def append_head(self, elem):
        # 插入元素
        # 插入到非空的队列里，始终保证一个队列为空（默认插入到队列A）
        queue = self.queue_B if self.queue_B else self.queue_A
        queue.append(elem)



def main():
    stack = Stack_with_Two_Queue()
    for i in range(3):
        stack.append_head(i)
    print(stack.queue_A)

    print(stack.delete_tail())
    print(stack.delete_tail())

    for i in range(3, 5):
        stack.append_head(i)
    print(stack.delete_tail())
    print(stack.delete_tail())
    print(stack.delete_tail())
    print(stack.delete_tail())


if __name__ == '__main__':
    main()
