# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         精益求精-递归的形参-减少位运算次数.py
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


import time
import copy

class Queen():

    def nqueens(self, n):
        self.sol = [0] * n  # 存储每行放置皇后的位置
        self.count = 0  # 解法总数

        tic = time.time()
        self.DFS(0, 0, 0 ,0,  n)  # 深度优先搜索,从第0行开始
        toc = time.time()
        total_time = toc - tic
        print("解法总数： ", self.count, '， 用时： ', total_time)

    def DFS(self, row, shu, pie, na, n):

        # 找到所有可行位置，用1表示
        # 之前是一步到位，求得所有位置
        # 现在一次只需要求一步
        ok = (~(shu | pie | na ))  & ((1 << n) -1)

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
                self.print_queen() # 打印结果
            else:
                # 不需要每次显式地修改状态——放在形参里面修改
                # 向下一行搜索
                self.DFS(row + 1, shu^p, (pie^p)>>1, (na^p)<<1,  n)  # 这一行找到合理的位置了，继续递归、检查下一行

    def print_queen(self):
        print("解法 ", self.count, ": ", end=' ')
        print(self.sol, end=' ')
        print()


def main():
    x = Queen()
    x.nqueens(8)

if __name__ == '__main__':
    main()