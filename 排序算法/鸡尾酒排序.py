# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         鸡尾酒排序.py
# Author:       wdf
# Date:         11/25/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  相当于对冒泡排序的一种改进
# Usage：
#-------------------------------------------------------------------------------

# 为了解决类似于[2,3,4,5,6,7,8,1]的排序问题，如果用冒泡排序，需要8轮
# 冒泡排序是从左到右
# 鸡尾酒排序就像钟摆，第一轮从左到右，第二轮从又到左，第三轮从左到右……

# 它能发挥出优势的场景， 是大部分元素已经有序 的情况。

def cocktail_sort(lst):
    for iter in range(len(lst) //2 ):

        flag = True
        # 从左到右, 完成后，最大值移动到最右边
        for i in range(len(lst) - iter - 1):# -iter表示iter次遍历后，后面的元素均有序
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                flag = False
        print(iter, lst)
        # 从右往左， 完成后，最小值移动到最左边
        for i in range(len(lst)-1 - iter, 0 + iter, -1):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                flag = False
        print(iter, lst)

        if flag: # 没有发生交换，说明已经有序
            break
    return lst


# unittest
import unittest
class TestCocktileSort(unittest.TestCase):
    def test_cocktail_sort(self):
        import random
        for i in range(10):
            lst = random.sample(range(20), 10)
            lst_copy = lst[:]
            self.assertEqual(cocktail_sort(lst), sorted(lst_copy))

def main():
    import random
    lst = random.sample(range(20), 10)
    print(lst)
    print(cocktail_sort(lst))

if __name__ == '__main__':
    unittest.main(verbosity=2)
    main()