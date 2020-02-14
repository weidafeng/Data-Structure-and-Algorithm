#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/6/2020 5:41 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        20. 表示数值的字符串
# description:      判断一个字符串是否表示数值（包括整数和小数）
# usage:            
# 如 +100  5e2  -123  3.14  -1e-6 都是
# 但 12e  1e3.14  1.2.3  +-5  12e5.4 都不是



# 简单的逻辑判断，要求考虑全面
def is_num(s):
    # e 和 . 字符最多有一次
    # e后面不能为空，或者有小数点
    if len(s) == 0:
        return False

    # 设置标记位，表示是否出现过这些特殊负号
    has_e, has_dot, has_sign = False, False, False

    # 逐个字符遍历
    for i in range(len(s)):

        # 指数e
        if s[i] == 'e' or s[i] == 'E':
            if has_e:  # e只能出现一次， 如果已经出现过e，则报错
                return False
            else:  # 如果是第一次出现e， e之后不能为空
                has_e = True
                if i == len(s) - 1:
                    return False

        # 小数点 .
        elif s[i] == '.':
            if has_dot:  # 小数点也只能出现一次
                return False
            else:  # 且e后面不能出现小数点
                has_dot = True
                if has_e:
                    return False

        # 正负号
        elif s[i] == '+' or s[i] == '-':
            if has_sign:
                # 如果前面已经出现过正负号，那这个正负号只能出现在e的后面一位
                if s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False

            if i != 0:
                # 如果是第一次出现符号位，且不是第一个，那必须在e后面
                if s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            has_sign = True

        else:
            # 要求字符为数字
            if '0' > s[i] or s[i] > '9':
                return False
    return True


def main():
    strings = ['+100', '5e2', '-123', '3.14', '-1e-6', '.23',
               '12e', '1e3.14', '1.2.3', '+-5', '12e5.4']
    for s in strings:
        print(is_num(s))


if __name__ == '__main__':
    main()
