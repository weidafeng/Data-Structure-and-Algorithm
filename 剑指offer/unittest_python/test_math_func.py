# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         test_math_func.py
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

import unittest
from math_func import *

class TestMathFunc(unittest.TestCase): #

    def test_add(self):
        self.assertEqual(3, add(1,2),msg='1+2=3')
        self.assertNotEqual(3,add(1,1),msg='1+1 != 3')

    def test_minus(self):
        self.assertEqual(minus(2,3), -1, msg='minus: 2-3 == 1')

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(3, 3))  # 错误

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

def main():  # 文件名以test开头，即使设置了main函数也不会执行
    print("wdf*********************************")
    print(add(1,2))
    print(minus(2,3))


if __name__ == '__main__':
    # unittest.main()
    unittest.main(verbosity=2)