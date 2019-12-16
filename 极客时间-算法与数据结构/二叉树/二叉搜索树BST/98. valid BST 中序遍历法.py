# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         98. valid BST 中序遍历法.py
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

# 二叉搜索树，binary search tree

# 左子树都小于根节点
# 右子树都大于根节点

# 可以用中序遍历的方法——中序遍历结果是升序数组，则为BST
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    '''
    Success
    Details
    Runtime: 60 ms, faster than 15.35% of Python3 online submissions for Validate Binary Search Tree.
    Memory Usage: 16 MB, less than 27.59% of Python3 online submissions for Validate Binary Search Tree.
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        order_result = self.inorder(root)
        # 比较中序遍历结果是否为升序
        return order_result == sorted(set(order_result)) # set去重，是因为BST不允许元素重复（否则非法）

    def inorder(self, root):
        # 中序遍历
        if root == None:
            return [] # 把遍历结果保存在数组里
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


class Solution2:
    '''
    Success
    Details
    Runtime: 52 ms, faster than 56.63% of Python3 online submissions for Validate Binary Search Tree.
    Memory Usage: 15.3 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
    优化，中序遍历时，不需要保存所有遍历结果——极大节省内存
    只需要前继节点，与当前节点进行比较
    
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None # 只需保存当前节点的前继节点，初始为空
        return self.helper(root)

    def helper(self, root):
        '''中序遍历，不需要保存所有遍历结果，只需要保留当前节点的前继节点'''
        if root == None:
            return True # 空树为BST
        if not self.helper(root.left): # 如果左子树不满足条件
            return False
        # 考虑右子树（之前）， 先进行判断，看右子树根节点的值是否更大
        if self.prev and self.prev.val >= root.val: # 如果当前节点存在前继节点，且值比前继节点更小
            return False
        
        self.prev = root # 把当前节点置为前继节点
        return self.helper(root.right)

def main():
    tree = TreeNode(
                    TreeNode(30,  # root
                             TreeNode(10, None, None), # left
                             TreeNode(40, None, None))) # right
    s = Solution()
    print(s.isValidBST(tree))
    s2 = Solution2()
    print(s2.isValidBST(tree))
if __name__ == '__main__':
    main()