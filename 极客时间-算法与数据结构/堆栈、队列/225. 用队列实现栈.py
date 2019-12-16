# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         225. 用队列实现栈.py
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

# 队列： 先进先出
# 堆栈： 先进后出

from queue import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

    def top(self) -> int:
        """
        Get the top element.
        """

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
def main():
    pass


if __name__ == '__main__':
    main()