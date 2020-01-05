# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         以一当百-使用位运算（整数取代数组，记录冲突）.py
# Author:       wdf
# Date:         1/5/2020
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

# 思想：
# 用一个32位整数代替一个长度为32的布尔数组

# 模拟数组操作(bit array)：
#     把第 i 位置1：a |= (1 << i);
#     把第 i 位置0：a &= ~(1 << i);
#     把第 i 位取反：a ^= (1 << i); ——常用
#     读取第 i 位的值：(a >> i) & 1; ——常用
#


import time


class Queen():

    def nqueens(self, n):
        self.sol = [0] * n  # 存储每行放置皇后的位置
        self.count = 0  # 解法总数

        ########## 记录冲突的二进制（不需要开辟数组，用int整数的二进制形式记录）
        self.shu, self.pie, self.na = 0, 0, 0

        tic = time.time()
        self.DFS(0, n)  # 深度优先搜索,从第0行开始
        toc = time.time()
        total_time = toc - tic
        print("解法总数： ", self.count, '， 用时： ', total_time)

    def DFS(self, row, n):
        # 遍历每一列，找到可以放置的位置
        for col in range(n):

            j = row + col # 撇的编号
            k = n - 1 + col - row # 捺的编号

            # 判别冲突
            # 用位运算[（a >> i ) & 1 ]取到那一位，如果有一个为1，则说明冲突
            if ((self.shu >> col | self.pie >> j | self.na >> k) & 1 ) != 0:
                continue # 如果冲突了，则说明这一列不能放，退出本次循环，检查下一列

            # 没有发生冲突
            if row == n - 1:
                self.count += 1
                self.print_queen() # 打印结果
            else:
                # 1. 修改状态 (此时已经知道那一位都是0，这样才能放置， 0与1异或 等于1），相当于修改状态
                self.shu ^= 1 << col
                self.pie ^= 1 << j
                self.na ^= 1 << k

                # 2. 放置皇后
                self.sol[row] = col  # 在第row行的col列放置皇后

                # 3. 向下一行搜索
                self.DFS(row + 1, n)  # 这一行找到合理的位置了，继续递归、检查下一行
                # 4. 复原状态(此时已经知道那一位都已经修改为1， 1与1异或 等于0），相当于清除状态
                self.shu ^= 1 << col
                self.pie ^= 1 << j
                self.na ^= 1 << k


    def print_queen(self):
        print("解法 ", self.count, ": ", end=' ')
        print(self.sol, end=' ')
        print()


def main():
    x = Queen()
    x.nqueens(8)


if __name__ == '__main__':
    main()