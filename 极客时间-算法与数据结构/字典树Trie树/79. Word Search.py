# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         79. Word Search.py
# Author:       wdf
# Date:         1/2/2020
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

# https://leetcode.com/problems/word-search/
# 79. Word Search
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
#     [
#       ['A','B','C','E'],
#       ['S','F','C','S'],
#       ['A','D','E','E']
#     ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


# 直接使用212的方法，给输入的word构建一个tire树，然后对board深度优先访问
# Success
# Details
# Runtime: 384 ms, faster than 37.39% of Python3 online submissions for Word Search.
# Memory Usage: 13.9 MB, less than 95.74% of Python3 online submissions for Word Search.
class Solution:
    def __init__(self):

        # 表示上下左右四个方向
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

        # 存储结果
        self.result = set()

        # tire树的终止符
        self.end_of_word = '#'

    def exist(self, board: list, word: str) -> bool:
        print(board, word)

        # 构建一个tire树
        self.root = {}
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.end_of_word] = self.end_of_word


        # 深度优先搜索
        # 遍历board的行和列
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.root: # 如果当前字符在tire树的前缀里（如果第一个字符就不满足，则不需要再判断后面的）
                    self.dfs(board, i, j, '', self.root)

        # 如果没有找到，则返回一个空set
        # print(self.result)
        return word in self.result


    def dfs(self,board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]] # 移动到下一层tire树

        if self.end_of_word in cur_dict:
            self.result.add(cur_word)
            return True  # 这个return不能跳出递归环节、终止程序

        tmp, board[i][j] = board[i][j], '@' # 临时变量存储当前位置的元素； 修改当前位置，表示该位置已经访问过

        for k in range(4): # 上下左右四个位置
            x, y = i + self.dx[k], j + self.dy[k]

            if 0<= x < len(board)  and 0<= y < len(board[0]) \
                and board[x][y] != '@' \
                and board[x][y] in cur_dict:
                if self.dfs(board, x, y, cur_word, cur_dict):  # 注意，这里很关键，一旦找到符合条件的，直接返回，避免后面多余的计算（否则会超时）
                    return True

        board[i][j] = tmp # 复原board


# 直接使用深度优先搜索
# Success
# Details
# Runtime: 356 ms, faster than 60.90% of Python3 online submissions for Word Search.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Word Search.
class Solution_2:
    def __init__(self):
        # 表示上下左右四个方向
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def exist(self, board: list, word: str) -> bool:
        # 为每一个字符在board里进行深度优先搜索
        # 深度优先搜索， 遍历board的行和列
        for i in range(len(board)):
            for j in range(len(board[0])):
                if  board[i][j] == word[0] and self._dfs(board, i, j, 0, word) : # 从第0个字符开始，在board里搜索word的每一个字符
                    return True
        # 如果没有找到（遍历完所有位置，都没有返回true），则返回False
        return False


    def _dfs(self, board, i, j, char_index, word):
        '''
        :param board:
        :param i:
        :param j:
        :param char_index:  查找到word的第char_index个字符
        :param word:  待查找的字符串
        :return:
        '''
        # 如果已经查找完word中的所有字符
        char_index += 1
        if char_index == len(word):
            return True

        tmp, board[i][j] = board[i][j], '@' # 临时变量存储当前位置的元素； 修改当前位置，表示该位置已经访问过

        for k in range(4):
            x, y = i + self.dx[k], j + self.dy[k]
            if 0<= x < len(board)  and 0<= y < len(board[0]) \
                and board[x][y] != '@' \
                and board[x][y] == word[char_index]:
                if  self._dfs(board, x, y, char_index, word):
                    return True
        board[i][j] = tmp # 复原board


def main():
    board = [   [ 'A', 'B', 'C', 'E'], \
                ['S', 'F', 'C', 'S'],  \
                ['A', 'D', 'E', 'E'] ]
    word = 'ABCCEDd'


    # x = Solution()
    # print(x.exist(board, word))
    #
    # board = [["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","b"]]
    # word = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    x = Solution_2()
    print(x.exist(board, word))

if __name__ == '__main__':
    main()