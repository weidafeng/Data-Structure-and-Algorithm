# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         235. Lowest Common Ancestor of a Binary Search Tree 最近公共祖先.py
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
#-------------------------------------------------------------------------------


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    与236题一样，找最近公共祖先

    可以直接用236题的方法，也可以针对二叉搜索树的特性进行优化


    Runtime: 68 ms, faster than 99.54% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':

        if p.val < root.val and q.val < root.val: # pq都小于根节点——说明pq都在左子树
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val: # 右子树
            return self.lowestCommonAncestor(root.right, p, q)

        # 一个在左，一个在右——公共祖先就是根节点
        return root

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode',
                              q: 'TreeNode') -> 'TreeNode':
        '''方法二，非递归实现
        Runtime: 72 ms, faster than 97.70% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
        Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
        '''

        while root:
            if p.val < root.val and q.val < root.val:  # pq都小于根节点——说明pq都在左子树
                root= root.left
            elif p.val > root.val and q.val > root.val:  # 右子树
                root= root.right
            else:
                # 一个在左，一个在右——公共祖先就是根节点
                return root


def main():
    pass


if __name__ == '__main__':
    main()