# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         102. Binary Tree Level Order Traversal树的层序遍历.py
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 广度优先搜索
# 常规思想
class Solution:
    def levelOrder(self, root: TreeNode):

        if not root:
            return []

        from collections import deque
        queue = deque()
        queue.append(root)

        # visited = set(root) # 加入已经访问的标志

        results = []  # 存放所有元素

        while queue:  # 不为空
            # print(queue)
            num_elem = len(queue)  # 本层元素个数
            level_result = []  # 存放本层元素
            for _ in range(num_elem):
                root = queue.popleft()
                level_result.append(root.val)

                if root.left:  # and  root.left in visited # 判断是否已经访问过
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            results.append(level_result)

        return results

############# 方法二
# Success
# Details
# Runtime: 32 ms, faster than 90.29% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13.4 MB, less than 67.74% of Python3 online submissions for Binary Tree Level Order Traversal.

# 深度优先搜索（递归实现）
# 记录层级level
# 先为每个层级新建好空数组、方便后续存储元素

# 时间复杂度与广度优先一致，都是O(n), 每个元素仅访问一次

# 深度搜索每个元素，把该元素放到对应层级的数组里
class Solution2:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, root, level):
        if not root:  # 递归终止条件
            return []

        if len(self.result) < level + 1:  # 为每一层开辟数组，用于存放结果
            self.result.append([])

        self.result[level].append(root.val) # 把当前层的结果放到对应数组里

        self._dfs(root.left, level + 1)  # 递归遍历做子树（这里不需要判断左右子树是否为空，因为开头已经写了递归终止条件）
        self._dfs(root.right, level + 1) # 递归遍历右子树


############ 方法三 列表生成式
# Details
# Runtime: 32 ms, faster than 90.29% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order
def levelOrder( root: TreeNode):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])  #  把当前level的值放入
        level = [kid for node in level for kid in (node.left, node.right) if kid ]  # 每次只放入当前level的左右孩子
    return ans


def main():
    res = []
    level = [1,3,5,7]
    for node in level :
        for kid in (node, node) :
            if kid:
                print(kid)
                res.append(kid)
    print(res)
if __name__ == '__main__':
    main()