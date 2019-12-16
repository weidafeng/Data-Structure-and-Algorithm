# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         生成器与迭代器.py
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

'''迭代器 iterator
list形式，一次性得到所有结果
'''
# 示例
l = [x*2 for x in range(10)]  # 中括号
print(type(l))
print(l)


'''生成器 generator
不必一次创建完整的list，而是一边执行一边生成，节省大量空间'''
# 示例
g = (x*2 for x in range(10)) # 小括号
print(type(g))
print(g)
print(next(g)) # 读取生成器的元素
print(next(g)) # 读取生成器的元素
print(next(g)) # 读取生成器的元素

for i in g:  # 此时只剩下后面的元素（前三个已经被next取出了）
    print(i, end=' ')

# 生成器的关键字不用return，而是用yield
def odd():
    print('step 1')
    yield 1  #每个next读取一个yield
    print('step 2')
    yield 3
    print('step 3')
    yield 5

############ 嵌套的列表生成式
print()
print("*"*10)
lst_pair = [(a,a*10) for a in range(5)]
print("lst_pair ",lst_pair)
print("嵌套列表生成式")
lst = [leaf for pair in lst_pair for leaf in pair if leaf]
'''
1. 遍历lst_pair的所有元素，记为pair
2. 遍历pair的所有元素， 记为leaf
3. 对leaf 加条件限制 if leaf
'''
# 等效于
result = []
for pair in lst_pair:
    for leaf in pair:
        if leaf:
            result.append(leaf)

print(lst)
print(result)



def main():
    print('\n\n\n')
    f = odd()
    print(next(f))
    print(next(f))
    print(next(f))
    # print(next(f)) # 再执行就会报错



if __name__ == '__main__':
    main()