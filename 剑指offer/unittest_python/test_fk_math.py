# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         test_fk_math.py
# Author:       wdf
# Date:         11/22/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  测试解方程组的各种情况
# Usage：
#-------------------------------------------------------------------------------
import unittest

from fk_math import *

class TestFkMath(unittest.TestCase):
    # 测试一元一次方程的求解
    def test_one_equation(self):
        # 断言该方程求解应该为-1.8
        self.assertEqual(one_equation(5 , 9) , -1.8)
        # 断言该方程求解应该为-2.5
        self.assertTrue(one_equation(4 , 10) == -2.5 , .00001)
        # 断言该方程求解应该为27/4
        self.assertTrue(one_equation(4 , -27) == 27 / 4)
        # 断言当a == 0时的情况，断言引发ValueError
        with self.assertRaises(ValueError):
            one_equation(0 , 9)
    # 测试一元二次方程的求解
    def test_two_equation(self):
        r1, r2 = two_equation(1 , -3 , 2)
        self.assertCountEqual((r1, r2), (1.0, 2.0), '求解出错')
        r1, r2 = two_equation(2 , -7 , 6)
        self.assertCountEqual((r1, r2), (1.5, 2.0), '求解出错')
        # 断言只有一个解的情形
        r = two_equation(1 , -4 , 4)
        self.assertEqual(r, 2.0, '求解出错')
        # 断言当a == 0时的情况，断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(0, 9, 3)
        # 断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(4, 2, 3)

def main():
    # 如果在pycharm里，不需要指定main函数，可以自动调用测试方法
    # 如果在命令行里，必须要指定，显式调用
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()