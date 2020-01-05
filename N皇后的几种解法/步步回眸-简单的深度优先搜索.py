# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         步步回眸-简单的深度优先搜索.py
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

# 深度优先搜索(Depth First Search)
# 依次枚举每行的皇后放在第几列
# 用一个整型数组存储已经放好的皇后的位置
# 枚举时现场检查冲突
#
# 慢！
# 检查冲突时需要检查上方的每一行

import time


class Queen():

    def nqueens(self, n):
        self.sol = [0] * n  # 存储每行放置皇后的位置
        self.count = 0  # 解法总数
        tic = time.time()
        self.DFS(0, n)  # 深度优先搜索,从第0行开始
        toc = time.time()
        total_time = toc - tic
        print("解法总数： ", self.count, '， 用时： ', total_time)

    def DFS(self, row, n):
        # 遍历每一列，找到可以放置的位置
        for col in range(n):
            ok = True  # 有效标识，初始化为可以放置
            # 遍历第0行到当前行的上一行——检查上面的每一行——慢的根源
            for i in range(row):
                # 检查冲突(列、撇、捺）
                if col == self.sol[i] \
                        or col - self.sol[i] == row - i \
                        or col - self.sol[i] == i - row:
                    ok = False
                    break  # 技巧，提前退出，前面的行冲突了，后面的行不需要考虑（对不对都不行）
            # 如果检查到冲突，说明这一列不能放，跳出去、考虑下一列
            if not ok:
                continue
            # 没有发生冲突
            self.sol[row] = col  # 在第row行的col列放置皇后
            if row == n - 1:
                self.count += 1
                # self.print_queen() # 打印结果
            else:
                self.DFS(row + 1, n)  # 这一行找到合理的位置了，继续递归、检查下一行

    def print_queen(self):
        print("解法 ", self.count, ": ", end=' ')
        print(self.sol, end=' ')
        print()


def main():
    x = Queen()
    x.nqueens(8)


if __name__ == '__main__':
    main()