# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         单元测试demo.py
# Author:       wdf
# Date:         11/22/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description: 整体流程
# 写好TestCase，
# 然后由TestLoader加载TestCase到TestSuite，
# 然后由TextTestRunner来运行TestSuite，
# 运行的结果保存在TextTestResult中，
# 我们通过命令行或者unittest.main()执行时，
# main会调用TextTestRunner中的run来执行，
# 或者我们可以直接通过TextTestRunner来执行用例。
# 原文链接：https://blog.csdn.net/huilan_same/article/details/52944782
# Usage：
#-------------------------------------------------------------------------------

import unittest

class TestCase_01(unittest.TestCase): # 继承unittest.TestCase

    '''
    如果我的测试需要在每次执行之前准备环境，
    或者在每次执行完之后需要进行一些清理怎么办？

    比如执行前需要连接数据库，
    执行完成之后需要还原数据、断开连接。
    '''
    @classmethod
    def setUpClass(cls) -> None:
        print("=====这是所有case的前置条件，每次运行程序会调用一次=====")

    @classmethod  # 注意，@classmethod不能漏，不然会报错
    def tearDownClass(self) -> None:
        print("====这是所有case的后置条件，每次运行结束，会调用一次====")

    def setUp(self) -> None:
        print("**** 这是每条case的前置条件，运行每个case都会调用一次 ****")

    def tearDown(self) -> None:
        print("**** 这是每条case的后置条件，运行每个case之后都会调用一次 ****")

    def test_01(self):  # 每条测试case都需要以test 开头
        print('test01, the first test case')

    def test_02(self):
        print('test02, the second test case ')

    @unittest.skip('不执行这条语句，原因是{测试}') # 可以跳过某条测试，也可以设置跳过的条件
    def test_03(self):
        print('test03, skip this test case')

    def test_04(self):
        print('test04, the forth test case')

def main():
    # 开始测试，方法一
    # 直接运行，啥都不需要指定，unittest自动测试所有
    # 比如在任意空白地方右键、run

    # 方法二
    # unittest.main()

    # 方法三
    # 将按照添加的顺序运行
    suite = unittest.TestSuite()
    suite.addTest(TestCase_01('test_01'))
    suite.addTest(TestCase_01('test_02'))
    suite.addTest(TestCase_01('test_03'))
    suite.addTest(TestCase_01('test_04'))
    # unittest.TextTestRunner().run(suite) # 直接运行

    # 或
    # 输出日志写入文件
    with open('wdf_单元测试demo_result.txt', 'w', encoding='utf-8') as f:
        unittest.TextTestRunner(stream=f,verbosity=1).run(suite)



if __name__ == '__main__':
    main()