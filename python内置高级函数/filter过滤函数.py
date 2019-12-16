# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         filter过滤函数.py
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
# -------------------------------------------------------------------------------

# 设置过滤条件
def condition(num):
    if num > 5 and num < 10:
        return num


lst = [12, 50, 8, 17, 9, 5]
result = filter(condition, lst)
print(result)
for i in result:
    print(i)

def main():
    pass


if __name__ == '__main__':
    main()
