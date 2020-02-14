# 55. 二叉树的深度
# 输入一棵二叉树的根节点, 求该树的深度(从根节点到叶子节点,最长的那条路径的长度称为深度)


# 两个临时变量,一个记录当前的深度,另一个记录最大的深度

class Node(object):
    '''节点类 '''
    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

def get_the_depth_of_tree(root):
    if root is None:
        return 0
    left = get_the_depth_of_tree(root.lchild) + 1
    right = get_the_depth_of_tree(root.rchild) + 1

    return max(left, right)

def main():
    root = Node(5,
                Node(3, Node(2), Node(4)),
                Node(7, Node(6), Node(8)))
    print(get_the_depth_of_tree(root))


    root = Node('D',
                Node('B', Node('A')),
                Node('E', rchild=Node('G', Node('H'))))
    print(get_the_depth_of_tree(root))


if __name__ == '__main__':
    main()

