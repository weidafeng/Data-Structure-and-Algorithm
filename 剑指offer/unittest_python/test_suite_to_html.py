# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         test_suite_to_html.py
# Author:       wdf
# Date:         11/22/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

'''
!!! 未测试!!!

HTMLTestRunner是一个第三方的unittest HTML报告库，首先我们下载HTMLTestRunner.py，并放到当前目录下，或者你的’C:\Python27\Lib’下，就可以导入运行了。

下载地址：


  官方原版：http://tungwaiyip.info/software/HTMLTestRunner.html

  灰蓝修改版：HTMLTestRunner.py(已调整格式，中文显示）
'''

import unittest
from test_math_func import TestMathFunc
from HTMLTestRunner import HTMLTestRunner

def main():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc)) # 自动加载所有测试样例

    with open('wdf_HTML_result.html', 'w') as f:
        runner = HTMLTestRunner


if __name__ == '__main__':
    main()