# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         BloomFilter.py
# Author:       wdf
# Date:         1/7/2020
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
# -------------------------------------------------------------------------------

# 手动实现布隆过滤器
# https://www.jianshu.com/p/aeffd84f540c


# 二进制数组（官方库）
# mmh3 哈希函数（第三方）
from bitarray import bitarray
import mmh3

'''MurmurHash哈希
MurmurHash是一种非加密型哈希算法，一般用于哈希检索操作。
是Austin Appleby在2008年发明的，并出现了多个变种版本，
当前版本是MurmurHash3,能够产生出32-bit或128-bit的哈希值。
这种哈希算法对于随机分布特征表现更加优良，被广泛运用redis、Hadoop等。

在布隆过滤器中的哈希算法就是采用这种算法
在python包中 mmh3 这个第三方包就是MurmurHash
pip install mmh3
'''

class BloomFilter(set):  # 继承自set

    def __init__(self, size, hash_count):
        '''

        :param size: bitarray 的长度，越大越不容易出错
        :param hash_count:  hash函数的个数，越大越不容易出错
        '''
        super(BloomFilter, self).__init__()
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)  # 初始化为全0

        self.size = size
        self.hash_count = hash_count

    def __len__(self):  # len()函数
        return self.size

    def __iter__(self):
        return iter(self.bit_array)

    def add(self, item):

        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] ^= 1 << index  # 位运算 置一

    def __contains__(self, item):  # 重写in方法
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            if self.bit_array[index] == 0:
                return False
        return True


def main():
    bloom = BloomFilter(100,5)
    lst = ['312','231','213','231','312']
    for num in lst:
        print(num)
        print(num in bloom)
        bloom.add(num)





if __name__ == '__main__':
    main()
