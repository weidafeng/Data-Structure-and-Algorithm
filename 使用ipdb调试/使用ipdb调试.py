#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/24/2020 11:52 PM
# software:         PyCharm
# project name:     Data Structure and Algorithm 
# file name:        使用ipdb调试.py
# description:      
# usage:            

# 第一种使用方法， 在代码里面加入断点

import ipdb


def main():
    # some code
    x = 10
    ipdb.set_trace()
    y = 20
    # other code


if __name__ == '__main__':
    main()
