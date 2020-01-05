# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         雁过留痕-深度优先搜索-记录冲突.py
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
# -------------------------------------------------------------------------------


# 深度优先搜索(Depth First Search)
# 依次枚举每行的皇后放在第几列
# 用三个布尔数组(boolean array)记录每一竖、撇、捺是否已被占用，随时更新
#
# 快了！
# 检查冲突为O(1)

import time


class Queen():

    def nqueens(self, n):
        self.sol = [0] * n  # 存储每行放置皇后的位置
        self.count = 0  # 解法总数

        ########## 记录冲突的数组, 一共n个列、2n-1个撇、2n-1个捺
        self.shu, self.pie, self.na = [0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1)

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
            if self.shu[col] \
                or self.pie[j] \
                or self.na[k]:
                continue # 如果冲突了，则说明这一列不能放，退出本次循环，检查下一列

            # 没有发生冲突
            if row == n - 1:
                self.count += 1
                # self.print_queen() # 打印结果
            else:
                # 1. 修改状态
                self.shu[col] = True
                self.pie[j] = True
                self.na[k] = True

                # 2. 放置皇后
                self.sol[row] = col  # 在第row行的col列放置皇后

                # 3. 向下一行搜索
                self.DFS(row + 1, n)  # 这一行找到合理的位置了，继续递归、检查下一行
                # 4. 复原状态
                self.shu[col] = False
                self.pie[j] = False
                self.na[k] = False
    def print_queen(self):
        print("解法 ", self.count, ": ", end=' ')
        print(self.sol, end=' ')
        print()


def main():
    x = Queen()
    x.nqueens(15)


if __name__ == '__main__':
    main()
