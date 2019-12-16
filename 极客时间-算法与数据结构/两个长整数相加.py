# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         两个长整数相加.py
# Author:       wdf
# Date:         11/29/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:
# Usage：
# -------------------------------------------------------------------------------

# python内部支持长整数相加
# 别的语言不支持

# 如需自己实现加法，可以按照小学数学列“竖式”的方法

def add_two_big_num(a, b):
    print(a, b)
    a, b = str(a), str(b)
    n = max(len(a), len(b))
    a, b = a.rjust(n+1, '0'), b.rjust(n+1, '0')  # 用0 补齐，长度+1（考虑进位）
    a, b = list(a)[::-1], list(b)[::-1]  # 倒序，方便从左到右地思考
    print(a, b)
    # 初始化结果数组，长度为a、b最长
    result = ['0'] * (n+1)

    for i in range(n):
        tmp = int(a[i]) + int(b[i]) + int(result[i])
        if tmp > 9:
            result[i] = str(tmp - 10)
            result[i+1] = '1'
        else:
            result[i] = str(tmp)
    print(result)
    return "".join(result[:-1])[::-1] if result[-1] == '0' else "".join(result)[::-1]


################
# 精简代码


def add_two_big_num_2(a, b):
    print(a, b)
    a, b = str(a), str(b)
    n = max(len(a), len(b))

    a, b = a.zfill(n+1), b.zfill(n+1) # Return the numeric string left filled with zeros in a string of length width.
    print(a, b)
    # 初始化结果数组，长度为a、b最长
    result = ['0'] * (n+1)
    for i in range(n, -1, -1): # 倒序，从后往前
        tmp = int(a[i]) + int(b[i]) + int(result[i])
        if tmp > 9:
            result[i] = str(tmp - 10)
            result[i-1] = '1'
        else:
            result[i] = str(tmp)
    print(result)
    return "".join(result[1:]) if result[0] == '0' else "".join(result)

def main():
    a= 426709752318
    b= 95481253129

    result = add_two_big_num(a, b)
    print(result)
    print(int(result) == (a+b))
    result = add_two_big_num_2(a, b)
    print(result)
    print(int(result) == (a+b))

if __name__ == '__main__':
    main()
