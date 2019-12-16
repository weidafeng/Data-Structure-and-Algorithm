# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         22. Generate Parentheses 生成合法的括号对.py
# Author:       wdf
# Date:         12/12/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------


# 22. Generate Parentheses
# Runtime: 28 ms, faster than 96.45% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Generate Parentheses.

class Solution:
    def generateParenthesis(self, n: int):
        # 关键思路： 左括号的数目一定大于等于又括号
        # 递归，遍历所有可能的情况
        self.lst = []  # 存储结果
        self._gen(0, 0, n, '')  # 初始状态，左括号用了0个，右括号用了0个，当前结果为空""
        return self.lst

    def _gen(self, left, right, n, result):
        '''
        left: 左括号用了几个
        right: 又括号用了几个
        n： 一共n个括号
        result： 存储当前结果
        '''
        print(left,right,"result:  ",result)
        if left == n and right == n:  # 左右括号都用完——一种合法的情况， 放入结果lst中
            self.lst.append(result)
            print("lst: ", self.lst)

            return  # 回溯到上一层（左括号减一，右括号为0）

        if left < n:
            self._gen(left + 1, right, n, result + "(")

        if right < n and right < left:  # 右括号还没用完，且不超过左括号的数
            self._gen(left, right + 1, n, result + ")")


################
# 改写为“当前剩余几个括号”
# 参见图解
'''
https://www.youtube.com/watch?v=sz1qaKt0KGQ

Runtime: 24 ms, faster than 99.18% of Python3 online submissions for Generate Parentheses.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Generate Parentheses.
'''
class Solution2:
    def generateParenthesis(self, n: int):
        # 关键思路： 左括号的数目一定大于等于又括号
        # 递归，遍历所有可能的情况
        lst = []  # 存储结果
        self._gen(n, n, '', lst)  # 初始状态，左括号还有n个可用，右括号还有n个可用，当前结果为空""
        return lst

    def _gen(self, left, right, cur_res, lst):
        '''

        :param left: 左括号还有n个可用
        :param right: 右括号还有n个可用
        :param cur_res:  当前结果
        :param result:  最终结果
        :return:
        '''
        print(left,right,"result:  ",cur_res)

        if left == 0 and right == 0:  # 左右括号都用完——一种合法的情况， 放入结果lst中
            lst.append(cur_res)
            print("lst: ", lst)

            return  # 回溯到上一层（左括号减一，右括号为0）

        if left:
            self._gen(left - 1, right, cur_res + "(", lst)

        if right  and right > left:  # 右括号还没用完，且剩余的右括号超过左括号的数
            self._gen(left, right - 1, cur_res + ")", lst)


def main():
    x = Solution2()
    x.generateParenthesis(3)


if __name__ == '__main__':
    main()