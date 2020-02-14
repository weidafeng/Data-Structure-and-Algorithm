# 二叉搜索树第k大节点
# 二叉搜索树: 根节点左边都比根节点小,右边都比根节点大
# 示例:
# 第三大节点是4

#             5
#     3               7
# 2       4       6       8
#

# 思路:
# 按照中序遍历的顺序遍历一棵二叉搜索树, 遍历序列的数值是递增排序的

class Node(object):
    '''节点类 '''
    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

class Solution:
    def __init__(self):
        self.result = []  # 存储中序遍历的结果

    def get_k_th_value(self, root, k):
        # self.in_order(root)  # 先进行中序遍历,保存结果到result数组中
        self.result = self.in_order_2(root)
        if k <= 0:
            return None
        if k > len(self.result):
            raise Exception('Out of range!')

        return self.result[k-1]  # 输出数组中的第k个数字


    def in_order(self, root):
        '''
        中序遍历, 把结果保存在result中

        :param k:   # 求第k大的元素
        :return:
        '''
        if root is None:
            return

        if root.lchild:
            self.in_order(root.lchild)

        self.result.append(root.value)

        if root.rchild:
            self.in_order(root.rchild)


    def in_order_2(self, root):
        # 中序遍历 代码精简
        if root is None:
            return []

        return self.in_order_2(root.lchild) + [root.value] + self.in_order_2(root.rchild)



def main():
    root = Node(5,
                Node(3, Node(2), Node(4)),
                Node(7, Node(6), Node(8)))
    print('中序遍历')
    x = Solution()
    print(x.get_k_th_value(root, 3))
    print(x.get_k_th_value(root, 0))
    print(x.get_k_th_value(root, 7))
    print(x.get_k_th_value(root, 1))
    print(x.get_k_th_value(root, 19))
    print()


if __name__ == '__main__':
    main()
