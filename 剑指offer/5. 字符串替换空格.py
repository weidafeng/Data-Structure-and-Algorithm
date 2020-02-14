#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         1/20/2020 9:31 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        5. 字符串替换空格
# description:      把字符串中的空格用“%20”替换（0X20是空格的ASCII码的十六进制形式）。 要求在原字符串上替换
# usage:            


def relpace_space_with_string(s):
    '''
    字符串的内置方法 replace——但该方法会开辟一个新的字符串，并非在原字符串上修改
    :param s: 字符串
    :return:
    '''
    return s.replace(' ', '%20')


def relpace_space_with_string_2(s):
    '''
    # 方法二
    逐一比较、替换
    :param s: 字符串
    :return:
    '''
    res = ''
    for i in s:
        if i == ' ':
            res += '%20'
        else:
            res += i
    return res


def relpace_space_with_string_3(s):
    # 方法二精简代码
    return ''.join([i if i != ' ' else '%20' for i in s])


############### 上面的方法都没有实现‘在原字符串上修改’的要求 ###############
## 在原字符串上替换，一个空格替换成三个字符，需要把后续的字符都往后移动

# 方法一，遇到一个空格，往后移动一次
def relpace_space_with_string_4(s):
    for i in range(len(s)):
        if s[i] == ' ':
            s = s + "  "  # 在后面添加两个空格
            idx = i
            while idx < 3:
                s[idx]
            while idx+3 < len(s) + 2:
                s[idx+3] = s[idx]
            s[i + 3:] = s[i + 1: -2]  # 把空格后面的向后移动2位
            s[i:i + 3] = '%20'
    return s


## 方法二，先记录下一共有几个空格、一次性开辟空间、从后往前移动
# 两个指针，一个指向字符串的最后一个字符，另一个指向开辟空间后的最后一个位置
# 依次移动，直到遇到空格时，只移动后面那个指针，用%20替换


def main():
    s = 'we are happy.'
    print(relpace_space_with_string(s))
    print(relpace_space_with_string_2(s))
    print(relpace_space_with_string_3(s))
    print(relpace_space_with_string_4(s))


if __name__ == '__main__':
    main()
