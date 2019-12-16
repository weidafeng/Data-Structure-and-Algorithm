# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         232. 用栈实现队列.py
# Author:       wdf
# Date:         11/10/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

# 用栈结构(FILO)，实现队列结构(FIFO)
# 主要是三个函数：
#     1. push
#     2. pop
#     3. peek

# 思路： 需要使用两个栈A, B
# 入栈push只从栈A，
# peek、pop只从栈B

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack, self.outstack = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.instack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.outstack: # 栈B不为空，直接从B弹出元素
            return self.outstack.pop()
        if self.instack: # 栈B为空，且栈A不为空，需要把栈A的元素都压到B
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
        # 下面思路有错误：只要B不为空，就应该直接从B 出栈，不需要先把所有A栈压到B栈
        # if self.instack: # 栈a不为空
        #     while self.instack: # 先把栈a清空、都放到栈b中
        #         self.outstack.append(self.instack.pop())
        # return self.outstack.pop() # 再从栈b pop

    def peek(self) -> int:
        """
        Get the front element.
        """
        # # 同样的，这个peek也错了
        # if self.instack: # 栈a不为空
        #     while self.instack: # 先把栈a清空、都放到栈b中
        #         self.outstack.append(self.instack.pop())
        # return self.outstack[-1]  # 再从栈b pop

        # 为了节省代码量，采用一种取巧的方法：
        # 调用pop（）
        # 再把这个值push进去
        val = self.pop()
        self.push(val)
        return val


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (not self.instack) and  (not self.outstack) # 两个栈都不为空


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


def main():

    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()  # 1
    obj.push(4)
    param_5 = obj.pop() # 2
    param_3 = obj.peek()  # 3
    param_4 = obj.empty()

    print(param_2, param_5, param_3, param_4)

if __name__ == '__main__':
    main()