# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         弹无虚发-使用位运算-只枚举可行位置，而不是枚举所有位置再判断是否可行.py
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

# 不要枚举每个位置并检查冲突
# 直接枚举不冲突的位置
#
#
# 在第row行：
#     竖冲突的位置：shu
#     撇冲突的位置：pie >> row
#     捺冲突的位置：na >> (n – 1 – row)
#
# 取最后一个1的位置：
#   a & -a


import time
import copy 

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

        # 找到所有可行位置，用1表示
        # 先是竖撇捺或运算，找到所有1——不能放的位置
        # 再取反—— 此时1 表示所有能放的位置
        # 再截取有效位（int整形有32位，前面没用）
        #    ~(  竖    |      撇           |           捺              )   &  只取用得到的位（int整形有32位，前面用不到）
        ok = (~(self.shu | (self.pie >> row) | (self.na >> (n - 1 - row))))  & ((1 << n) -1)

        # 不需要遍历每一列了，只需要遍历所有可行的位置
        while ok != 0:
            p = ok & -ok # 取最低位的1， p是个二进制串， 只有1位是1，其余都是0
            ok ^= p  # 清除该位（说明这个位置已经放过了、下次不能放了）
            # 没有发生冲突
            # 2. 放置皇后
            # p中的1的索引即为放置的位置
            col = 0
            p_copy = copy.deepcopy(p)
            while p_copy != 1:
                # print(p_copy)
                p_copy = p_copy >> 1
                col += 1
            self.sol[row] = col  # 在第row行的col列放置皇后

            if row == n - 1:
                self.count += 1
                # self.print_queen() # 打印结果
            else:
                # 1. 修改状态 (此时已经知道那一位都是0，这样才能放置， 0与1异或 等于1），相当于修改状态
                self.shu ^= p #与1 异或
                self.pie ^= p << row
                self.na ^=  p << n - 1 - row


                # 3. 向下一行搜索
                self.DFS(row + 1, n)  # 这一行找到合理的位置了，继续递归、检查下一行
                # 4. 复原状态(此时已经知道那一位都已经修改为1， 1与1异或 等于0），相当于清除状态
                self.shu ^= p  # 与1 异或
                self.pie ^= p << row
                self.na ^= p << n - 1 - row

    def print_queen(self):
        print("解法 ", self.count, ": ", end=' ')
        print(self.sol, end=' ')
        print()


def main():
    x = Queen()
    x.nqueens(15)


if __name__ == '__main__':
    main()