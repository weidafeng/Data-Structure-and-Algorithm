# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         98.valid BST 递归实现.py
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
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    '''递归实现，按照BST的定义'''
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root)

    def helper(self, root, min_val=None, max_val=None):
        '''
        效率最高的方法
        Runtime: 44 ms, faster than 86.90% of Python3 online submissions for Validate Binary Search Tree.
        Memory Usage: 15.2 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
        :param root: 根节点
        :param min_val:  当前子树所有值的下界
        :param max_val:  当前子树所有值的上界
        :return:
        '''
        if root == None:  # 空树，为真
            return True
        print(root.val)
        if min_val != None and root.val <= min_val: # 如果当前节点比最小值还小(注意，要写明!=None， 否则值为0的时候会报错）
            return False
        if max_val != None and root.val >= max_val: # 如果当前节点比最大值还大
            return False

        return self.helper(root.left, min_val, max_val=root.val) and  self.helper(root.right, root.val, max_val) # and， 左右子树均满足

def main():
    tree = TreeNode(
        TreeNode(30,  # root
                 TreeNode(10, None, None),  # left
                 TreeNode(40, None, None)))  # right
    s = Solution()
    print(s.isValidBST(tree))



if __name__ == '__main__':
    main()