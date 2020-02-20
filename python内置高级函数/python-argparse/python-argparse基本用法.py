#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/20/2020 10:01 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        python-argparse基本用法
# description:
# 使用说明： https://docs.python.org/zh-cn/3/howto/argparse.html
# api文档：https://docs.python.org/zh-cn/3/library/argparse.html
# 中文教程： https://www.jianshu.com/p/fef2d215b91d
# usage:            


import argparse

# 第一步 创建一个ArgumentParser对象
parser = argparse.ArgumentParser(description='解释器对象')
# --help 选项，也可缩写为 -h，是唯一一个可以直接使用的选项（即不需要指定该选项的内容）
# 作用是打印所有命令，以及该命令的help


# 第二步 使用add_argument 添加参数

# 位置参数
parser.add_argument('first_place', default=None, help='调用时不需要使用--first_place', type=str)
parser.add_argument('second', help='输入正方形的边长，计算面积', type=int)

# 可选参数
parser.add_argument('-v', '--verbosity', help='可选参数，如果指定的话，必须要加参数， 如 -v 1')
parser.add_argument('-s', '--show', action='store_true',
                    help='store_true参数， 如果我们指定了--show，那么就给show赋值为True， 如果没有指定该参数，show就赋值为False')
# choice 指定选项
parser.add_argument('-d', '--day', choices=[1, 2, 3, 4, 5, 6, 7], help='指定参数范围', type=int)


# 第三步 解释参数
args = parser.parse_args()
print('第一个位置参数，echo：', args.first_place)  # 第一个位置参数
print('第二个位置参数，计算面积', args.second, args.second ** 2)

# 可选参数，顺序不重要
# 设置了可选参数时，需要指定值
# python python-argparse基本用法.py haha 3 -v 1  # 显示
# python python-argparse基本用法.py haha 3 -v 0  # 注意，即便是0，也显示！！！
if args.verbosity:
    print(args.verbosity, type(args.verbosity))  # 因为默认的输入类型是str， bool('0')是True
    print('设置了可选参数verbosity')
else:
    print('不显示')

# store参数
# python python-argparse基本用法.py haha 3 -s
# python python-argparse基本用法.py haha 3 -show
# python python-argparse基本用法.py haha 3
print(args.show, type(args.show))
if args.show:
    print('设置了可选参数show')
else:
    print('没有设置，则赋值为False')


# choice选项
# 限定了范围
if args.day == 6 or args.day == 7:
    print('周末')
else:
    print('工作日')


def main():
    pass


if __name__ == '__main__':
    main()
