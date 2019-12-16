# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         递归实现挖金矿问题.py
# Author:       wdf
# Date:         12/9/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
# -------------------------------------------------------------------------------

def get_best_gold_mining(w: int, n: int, p: list, g: list):
    '''
    递归方法求解（弊端：有大量重复计算，效率太低）
    :param w: 工人数量
    :param n: 可选金矿数量
    :param p: 金矿开采所需工人数量（list)
    :param g:  金矿储量（list）
    :return: 
    '''
    # 边界条件，工人数量为0，或金矿数量为0，则总收益为0
    if w == 0 or n == 0:
        return 0

    # 情况一
    # 所剩工人数不够开挖当前金矿，只有一种最优解
    if w < p[n - 1]: # n-1表示list索引，从0开始
        return get_best_gold_mining(w, n - 1, p, g)

    # 情况二（更普遍）
    # 挖当前金矿 与 不挖当前金矿
    return max(get_best_gold_mining(w, n - 1, p, g),  # 不挖当前金矿
               get_best_gold_mining(w - p[n - 1], n - 1, p, g) + g[n - 1]) # 挖当前金矿


# TODO 动态规划

# 非递归实现动态规划
# 动态规划的要点： 自底向上求解
def get_best_gold_mining2(w:int, p:list, g:list):
    '''
    非递归实现
    用二维数组存储结果
    :param w:
    :param p:
    :param g:
    :return:
    '''
    table = [[0]*(len(g)+1)] * (w+1)
    print(table)

    # 填充表格
    for i in range(1,len(g)+1):
        for j in range(1,w+1):
            if j < p[i-1]: # 剩余工人数不够挖当前金矿
                table[i][j] = table[i-1][j]
            else:
                table[i][j]= max(table[i-1][j], # 不挖当前金矿
                                 table[i-1][j-p[i-1]] + g[i-1])
        print(table)
    return table[-1][-1]

def main():
    w = 10  # 10个工人
    p = [5, 5, 3, 4, 3]  # 开采每个金矿所需的工人数
    g = [400, 500, 200, 300, 350] # 开采每个金矿得到的黄金数量
    print(get_best_gold_mining(w,len(g), p, g))
    print(get_best_gold_mining2(w, p, g))

if __name__ == '__main__':
    main()
