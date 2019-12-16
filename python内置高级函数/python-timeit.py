# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         python-timeit.py
# Author:       wdf
# Date:         12/15/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

import timeit

print(timeit.timeit(stmt='"_".join(str(n) for n in range(1000))',
                    setup='pass',
                    timer=timeit.default_timer, # 默认的计时器
                    number=1000) )
'''
stmt是要执行的代码，字符串形式，多行就多个字符串。
setup是执行前的环境配置，比如import语句。
timer是使用的计时器。
number是执行的次数。
globals是执行的命名空间。
'''

def test():
    """Stupid test function"""
    L = [i for i in range(100)]

print(timeit.timeit(stmt='test()',
                    setup="from __main__ import test", # 要加这一句，不然会报错：NameError: name 'test' is not defined
                    number=1000))


def test2():
    """Stupid test function"""
    L = [i for i in range(100)]

print(timeit.timeit(stmt='test2()',
                    globals=globals(), # 也可以通过globals（）指定参数的运行空间—— 比较方便
                    number=1000))



############ 同时测试多个函数， 使用globals() 更方便 ###########
def f(x):
    return x**2
def g(x):
    return x**4
def h(x):
    return x**8

import timeit
print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))



def main():
    pass


if __name__ == '__main__':
    main()