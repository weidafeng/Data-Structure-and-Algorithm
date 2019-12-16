# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         pythond的itertools库.py
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

import itertools

######################### accumulate 累加 ###############################
# 从第一个元素开始，逐个与后面的元素累加
# 数字累加
# 字符串拼接
x = itertools.accumulate(range(10))
print(x) # tertools.accumulate object
print(list(x)) # [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
print(list(itertools.accumulate(['a','b','c','d']))) #['a', 'ab', 'abc', 'abcd']





######################### chain 链接 ###############################
# 先遍历迭代第一个可迭代对象，如果第一个用完了，再考虑迭代第二个
# （等用到了才拼接）
print(itertools.chain('ABC', 'DEF') )#generator --> A B C D E F
for elem in itertools.chain('ABC','DEF'):
    print(elem, end=' ')
print()
# Make an iterator that returns elements from the first iterable until it is exhausted,
# then proceeds to the next iterable, until all of the iterables are exhausted.
# Used for treating consecutive sequences as a single sequence.

# Equivalent to:
def chain(*iterables):
    for it in iterables:
        for element in it:
            yield element

print(chain('ABC', 'DEF') )#generator --> A B C D E F
for elem in chain('ABC','DEF'):
    print(elem, end=' ')
print()

######################### combinations 组合 ###############################
# 从可迭代对象中得到长度为 r 的子序列
# 返回结果按照字典序
# 元素根据位置不同被认为是不同的元素，而不是元素的值
lst = ['a','b','c','d']
x = itertools.combinations(lst, r=len(lst))
print(x) #itertools.combinations object
print(list(x)) # 长度为元素个数的子序列，只有一个（它本身）


x = itertools.combinations(lst, r=3)
print(list(x)) # [('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]

# 元素值相同，也会被当成不同的元素（内部是以元素的位置区分不同的元素）
x = itertools.combinations([1,1,1,1], r=3)
print(list(x)) # [(1, 1, 1), (1, 1, 1), (1, 1, 1), (1, 1, 1)]



######################### combinations_with_replacement 组合(允许重复的元素） ###############################
x = itertools.combinations_with_replacement('ABC', 2)
print(x)
print(list(x)) #[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]



######################### compress 压缩/过滤器 ###############################
# 按照真值表筛选元素
# Make an iterator that filters elements from data returning only those that
# have a corresponding element in selectors that evaluates to True.

x = itertools.compress(data=range(5),selectors=(True, False, True, True, False))
print(x)
print(list(x)) # [0,2,3]

# equivalent to
def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    return (d for d, s in zip(data, selectors) if s)
x = compress(data=range(5),selectors=(True, False, True, True, False))
print(x)
print(list(x)) # [0,2,3]

######################### count 计数器 ###############################
# 计数器,可以指定起始位置和步长

print("*"*20)
x = itertools.count(start=1, step=2)
print(x) # count(1,2)
print(list(itertools.islice(x, 0, 10, 1)))  # Make an iterator that returns selected elements from the iterable

'''
itertools.cycle
循环指定的列表和迭代器

>>> x = itertools.cycle('ABC')
>>> print(list(itertools.islice(x, 0, 10, 1)))
['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']



'''


######################### dropwhile 组合 ###############################
# 按照真值函数丢弃掉列表和迭代器前面的元素

x = itertools.dropwhile(lambda e: e < 5, range(10))
print(list(x)) # [5, 6, 7, 8, 9]

# 类似功能的：
# itertools.filterfalse
# 保留对应真值为False的元素
# Return those items of sequence for which function(item) is false.
x = itertools.filterfalse(lambda e: e < 5, (1, 5, 3, 6, 9, 4)) #
print(list(x))  # [5, 6, 9]

######################### groupby 分组 ###############################
x = itertools.groupby(range(10), lambda x: x < 5  or x > 7)
print(x)
# print(list(x))  # [5, 6, 9]
for condition, data in x:
    print(condition, list(data))

######################### permulation 全排列 ###############################
# 产生指定数目的元素的所有排列(顺序有关)

x = itertools.permutations('ABC', 3)
print(x)
print(list(x)) # [0,2,3]

x = itertools.permutations('ABC', 2)
print(x)
print(list(x)) # [0,2,3]

'''
itertools.repeat
简单的生成一个拥有指定数目元素的迭代器

>>> x = itertools.repeat(0, 5)
>>> print(list(x))
[0, 0, 0, 0, 0]   



itertools.starmap
类似map

>>> x = itertools.starmap(str.islower, 'aBCDefGhI')
>>> print(list(x))
[True, False, False, False, True, True, False, True, False]



itertools.takewhile
与dropwhile相反，保留元素直至真值函数值为假。

>>> x = itertools.takewhile(lambda e: e < 5, range(10))
>>> print(list(x))
[0, 1, 2, 3, 4]

'''

def main():
    pass


if __name__ == '__main__':
    main()