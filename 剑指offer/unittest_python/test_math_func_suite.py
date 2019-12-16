# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         test_math_func_suite.py.py
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

# 问题二(test_math_func.py)只有一个测试文件，我们直接执行该文件即可
# 如果有多个测试文件，怎么进行组织，总不能一个个文件执行吧，答案也在TestSuite中。
from test_math_func import TestMathFunc
import unittest

def write_result_to_file():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    with open('wdf_test_math_func_result.txt','w',encoding='utf-8') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

def main():
    suite = unittest.TestSuite()

    # 顺序是按照我们添加进suite的顺序执行的。
    tests = [TestMathFunc('test_add'),
             TestMathFunc('test_divide'),
             TestMathFunc('test_minus'),              TestMathFunc('test_divide'),
             TestMathFunc('test_minus'),
             TestMathFunc('test_multi')]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main()
    write_result_to_file()