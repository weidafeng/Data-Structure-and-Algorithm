# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         20. 判断括号是否匹配.py
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

def is_valid(s):
    '''使用堆栈，左括号入栈，又括号判断是否有匹配'''
    stack = []
    for i in s:
        if i in ['(', '[', '{']:
            stack.append(i)
        elif (i == ")" and stack[-1] =="(") or (i == "]" and stack[-1] =="[") or (i == "}" and stack[-1] =="{"):
            stack.pop()
        else:
            return False
    return len(stack) == 0 # 最后如果栈空了，则说明所有都匹配

def is_valid_2(s):
    '''
    使用dict结构，精简代码
    :param s: 输入的括号字符串
    :return:
    '''
    param = {")": "(",
             "]":'[',
             "}":"{"}
    stack = []
    for i in s:
        if i not in param: #如果是左括号，则入栈
            stack.append(i)
        elif not stack or stack.pop() != param[i]: # 否则是有括号，如果栈为空，或者括号不匹配，则错误
            return False
    return not stack

def is_valid_3(s):
    '''方法三，字符串替换，去掉每一个成对的括号'''
    n = len(s) **2  # 循环一个较长的次数
    for i in range(n):
        s = s.replace("()","").replace("[]","").replace("{}", "")
    return not len(s)


def main():
    s = "{}[]()"
    s2 = "(([[]]))"
    s3 = "(([[]{]))"
    print(is_valid(s))
    print(is_valid(s2))
    print(is_valid(s3))

    print()
    print(is_valid_2(s))
    print(is_valid_2(s2))
    print(is_valid_2(s3))

    print()
    print(is_valid_3(s))
    print(is_valid_3(s2))
    print(is_valid_3(s3))


if __name__ == '__main__':
    main()