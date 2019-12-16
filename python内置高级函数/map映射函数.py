# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         map映射函数.py
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

'''将每个列表元素或字符串，都执行某个函数，结果以列表的形式返回

一般与lambda一起使用

'''

# 执行一个函数 x+y
res = map(lambda x,y: x+y, [1,2,3], [4,5,6]) # 把两个列表对应元素相加
print(res) # <map object at 0x000001904DACF828>

for i in res:
    print(i)

# 执行两个函数 x+y、 x*y
res = map(lambda x,y: (x+y, x*y) , [1,2,3], [4,5,6]) # 把两个列表对应元素相加
print(res) # <map object at 0x000001904DACF828>
for i in res:
    print(i)


#### map无法处理对应位置操作数类型不一致的情况
# 能处理多少处理多少
res = map(lambda x,y: (x+y, x*y) , [1,2,3], [4,5,'a']) # 把两个列表对应元素相加
print(res) # <map object at 0x000001904DACF828>
for i in res:
    print(i)  # 虽然最后的a类型不对，但前面的都会处理

#### map两个迭代数组长度不一致的情况，也是能处理多少处理多少
res = map(lambda x,y: (x+y, x*y) , [1,2,3], [4,5])  # 前面三个，后面两个
print(res) # <map object at 0x000001904DACF828>
for i in res:
    print(i)  # 最后少了一个元素（无法匹配），但前面的都会处理

def main():
    pass


if __name__ == '__main__':
    main()