# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         lambda匿名函数.py
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
'''
匿名函数， 比较简洁，不需要def定义函数
'''
#### 单个参数
# 两种写法
fun_1 = lambda x: x+1

def fun_2(x):
    return  x + 1

print(fun_1(10))
print(fun_1(100))

print(fun_2(10))
print(fun_2(100))


#### 多个参数
fun_3 = lambda x,y, z: (x+y) * z
print(fun_3(1,2,3))


fun_3 = lambda x,y, z: (x+y)  # 也可以传入三个参数、只使用部分参数运算
print(fun_3(1,2,3))


#############
# lambda表达式会返回一个函数对象， 如果没有变量接收这个返回值，则会被丢弃
# 但因为lambda只是一个表达式，所以可以直接作为list、dict的成员
lst = [lambda a: a**2, lambda b:b**3]
print(lst[0]) # <function <lambda> at 0x0000025E2936FEA0>

print(lst[0](3), lst[1](3))



##############利用lambda对字典求最大值、或排序
count_set =  {'a': 3, 'b': 2, 'c': 1}

# 直接求最大：
print(max(count_set))   # 默认key为关键字
# 结果； c

# 指定比较关键字
print(max(count_set.items(), key=lambda kv:kv[1])) # value为排序关键字
print(max(count_set.items(), key=lambda kv:kv[0])) # key 为排序关键字
# ('a', 3)
# ('c', 1)

##### 排序(SORTED 函数默认从小到大）
print(sorted(count_set.items(), key=lambda kv: kv[1]))
print(sorted(count_set.items(), key=lambda kv: kv[0]))
# [('c', 1), ('b', 2), ('a', 3)]
# [('a', 3), ('b', 2), ('c', 1)]
print(sorted(count_set.items(), key=lambda kv: (kv[0],kv[1]))) # 如果指定了两个，则先按第一个关键字排序，再按第二个



def main():
    pass


if __name__ == '__main__':
    main()