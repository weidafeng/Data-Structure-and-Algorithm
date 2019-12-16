# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         类方法、静态方法、普通方法.py
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

class Foo:
    def __init__(self, name):
        self.name = name

    def ordinary_func(self):
        '''定义普通方法， 至少有一个self参数'''
        print(self.name)
        print('普通方法')

    @classmethod
    def class_func(cls):
        '''定义类方法，需要用@classmethod修饰，且至少有一个cls参数'''
        print("类方法")

    @staticmethod
    def static_func():
        '''定义静态方法，无默认参数'''
        print("静态方法")


def main():
    foo = Foo('tristan')
    foo.ordinary_func() # 调用普通方法
    foo.class_func() # 调用类方法
    foo.static_func() # 调用静态方法

if __name__ == '__main__':
    main()