# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         删除K个数字后的最小值.py
# Author:       wdf
# Date:         11/29/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  给定一个整数，求删除k个数字后的最小值
# Usage：
# -------------------------------------------------------------------------------

# 原理：给出一个整数541 270 936 ， 要求删去1个数字， 让剩下的整数尽可能小。
# 此时， 无论删除哪一个数字， 最后的结果都是从9位整数变成8位整数。
# 既然同样是8位整数， 显然应该优先把高位的数字降低， 这样对新整数
# 的值影响最大

# 如何把高位的数字降低呢？ 很简单， 把原整数的所有数字从左到右进
# 行比较， 如果发现某一位数字大于它右面的数字， 那么在删除该数字
# 后， 必然会使该数位的值降低 ， 因为右面比它小的数字顶替了它的位
# 置。

def remove_one_num(num):
    flag = False  # 标识符，表示尚未删除元素
    for i in range(len(num) - 1):  # 从左到右遍历
        if num[i] > num[i + 1]:  # 如果高位比低位的值更大， 则删除高位的值
            del num[i]
            flag = True  # 删除了元素
            return num, flag
    # 若没有符合高位比低位大的元素，则删除最后一个
    del num[-1]
    return num, flag


def remove_k_nums(num, k):
    num = list(str(num))  # 转化成list，方便处理
    for i in range(k):
        num, flag = remove_one_num(num)

    return int(''.join(num))  # 转化回int


#####################################
# 方法二
# 利用堆栈的特性,以遍历数字作为外循环， 以k作为内循环，

# 因为方法一每次删除单个元素时，都要从左到右逐一遍历
# 如果数字是11111111190， 每次都得从头开始

'''
举例："541270936"，去除3个数字。
    5入栈，stack=[5]
    4入栈，判断4<5，5出栈，4入栈。stack=[4]。出栈一次，num=1
    1入栈，判断1<4，4出栈，1入栈。stack=[1]。出栈一次，num=2
    2入栈，判断2>1，2直接入栈。stack=[1,2]
    7入栈，判断7>2，7直接入栈。stack=[1,2,7]
    0入栈，判断0<7，7出栈，0入栈。stack=[1,2,0]。出栈一次，num=3。此时出栈了3次，相当于去除了3个数字。满足要求。那么剩下的字符就直接入栈就可以了。
剩余字符全部入栈。stack=[1,2,0,9,3,6]'''

def remove_k_num_2(num, k):
    num = list(str(num))
    if len(num) < k: return None

    stack = []
    for i in num:  # 遍历数组， 每次都入栈该元素，如果栈顶元素比当前元素大，则栈顶出栈
        print(k, stack)
        if not stack:
            stack.append(i)  # 初始化栈，放入最高位
            continue  # 跳出本次循环
        if k > 0:  # 需要删除k个元素
            while k > 0 and stack:
                if stack[-1] > i:  # 高位比低位大，则删除
                    stack.pop()
                    k -= 1
                else:  # 否则退出
                    break
        stack.append(i)  # 1） 高位比低位小，不删除； 2）高位比低位大，删除后，都需要把低位元素放入栈中
    if k != 0:  # 如果删除的元素不够（高位比低位都小，如1234567， 则删除删除最后的元素）
        return int(''.join(stack[:-k]))
    return int(''.join(stack))

def remove_k_num_wdf(num, k):
    num = list(str(num))
    stack = []
    for item in num:
        if not stack:
            stack.append(item)
            continue

        while k > 0 and stack:
            if stack[-1] > item:
                stack.pop()
                k -= 1
            else:  # 不满足出栈的条件（高位比低位小，不需要出栈）
                break

        stack.append(item)

    if k > 0:
        return ''.join(stack[:-k])
    return ''.join(stack)


def main():
    num = 541270936
    # print(remove_one_num(num))
    print(remove_k_nums(num, 7))
    print(remove_k_num_2(num, 3))
    print(remove_k_num_wdf(num, 3))


if __name__ == '__main__':
    main()
