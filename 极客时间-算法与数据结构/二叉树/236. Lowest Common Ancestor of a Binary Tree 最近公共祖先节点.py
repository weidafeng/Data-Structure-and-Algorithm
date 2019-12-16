# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         236. Lowest Common Ancestor of a Binary Tree 最近公共祖先节点.py
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    找到两个字数的最近公共祖先

    思路：
    如果从一个节点root开始往下搜索，既能搜到p，也能搜到q， 说明该root节点是其公共祖先，
    然后再找他们最近的公共祖先

    Runtime: 80 ms, faster than 72.21% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    Memory Usage: 23 MB, less than 91.67% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    '''

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':

        if root == None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p,
                                         q)  # 看看pq是否在左子树存在，结果放在left
        right = self.lowestCommonAncestor(root.right, p,
                                          q)  # 看看pq是否在右子树里存在， 结果放在right

        if left == None:  # 如果左边为空，说明结果肯定不在左边
            return right  # 递归调用，去右边寻找
        if right == None:  # 如果右边为空，说明结果肯定不在右边
            return left  # 递归调用，去左边寻找
        return root  # 左右均不为空，左边存在p和q，右边也存在p和q，说明该节点即为公共祖先节点



def main():
    pass


if __name__ == '__main__':
    main()
