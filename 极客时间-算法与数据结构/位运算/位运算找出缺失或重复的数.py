# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         位运算找出缺失或重复的数.py
# Author:       wdf
# Date:         12/8/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
# -------------------------------------------------------------------------------

# 在一个无序数组里有99个不重复的正整数， 范围是1～100， 唯独缺少1
# 个1～100中的整数。 如何找出这个缺失的整数？

def method1(lst):
    print(sum([i for i in range(1, 101)]) - lst)


# 问题扩展，对于有重复的数组
# 一个无序数组里有若干个正整数， 范围是1～100， 其中99个整数都出现
# 了偶数次 ， 只有1个整数出现了奇数次 ， 如何找到这个出现奇数次的整数
def method2(lst):
    # 异或
    # 所有出现偶数次的整数都会相互抵消变成0， 只有
    # 唯一出现奇数次的整数会被留下。
    from functools import reduce
    result = reduce(lambda a, b: a ^ b, lst)
    return result


lst = [1, 3, 2, 4, 5, 2, 1, 3, 4]
print(method2(lst))


# 问题扩展2
# 假设一个无序数组里有若干个正整数， 范围是1～100， 其中有98个整数
# 出现了偶数次， 只有2个 整数出现了奇数次， 如何找到这2个出现奇数
# 次的整数？

# 思路
# 首先把数组元素依次进
# 行异或运算， 得到的结果是2个出现了奇数次的整数的异或运算结
# 果， 在这个结果中至少有1个二进制位是1。
def method3(lst):
    '''
    把2个出现了奇数次的整数命名为A和B。 遍历整个数组， 然后依次做异
    或运算， 进行异或运算的最终结果， 等同于A和B进行异或运算的结
    果。 在这个结果中， 至少会有一个二进制位是1（如果都是0， 说明A和
    B相等， 和题目不相符） 。

    选定该结果中值为1的某一位数字， 如00000110B的倒数第2位是1， 这说
    明A和B对应的二进制的倒数第2位是不同的。 其中必定有一个整数的倒
    数第2位是0， 另一个整数的倒数第2位是1。

    根据这个结论， 可以把原数组按照二进制的倒数第2位的不同， 分成两
    部分， 一部分的倒数第2位是0， 另一部分的倒数第2位是1。 由于A和B
    的倒数第2位不同， 所以A被分配到其中一部分， B被分配到另一部分
    '''

    # 第一步，所有元素进行异或
    from functools import reduce
    xor_result = reduce(lambda a,b:a^b, lst)

    # 第二步，找到异或结果中为1的一位（分治依据）
    diff_index = 1 # 表示不同的那一位
    while xor_result & diff_index == 0:
        diff_index = diff_index << 1

    # 第三步，进行分组异或运算
    result = [0, 0]  # 初始为0，准备异或
    for elem in lst:
        if elem & diff_index:  # 第diff_index位为1 的分组
            result[0] ^= elem
        else:  # 为0 的分组
            result[1] ^= elem

    return result

lst = [1, 3, 2, 4, 5, 2, 1, 3, 4, 9]
print(method3(lst))


def main():
    pass


if __name__ == '__main__':
    main()
