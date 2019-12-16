# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         python手动实现二叉树.py
# Author:       wdf
# Date:         11/20/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  python 实现二叉树
#                         节点的构造
#                         树的构造
#                         递归实现先序遍历、中序遍历、后序遍历
#
#                         堆栈实现先序遍历
#                               中序遍历
#                               后序遍历（需两个堆栈）
#                         队列实现层次遍历
# Usage：
# -------------------------------------------------------------------------------

'''参考教程：https://blog.csdn.net/bone_ace/article/details/46718683
特别详细'''
########## 树的构造

class Node(object):
    '''节点类 '''
    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


# 构造树
class Tree(object):
    '''二叉树类'''
    def __init__(self):
        self.root = Node()
        self.my_queue = []  # 存储各个节点

    def add(self, value):
        '''为树添加节点'''
        node = Node(value) # 初始化一个节点
        if self.root.value == None: # 如果树是空的，则该节点为根节点
            self.root = node
            self.my_queue.append(self.root)

        else:   # 不是空树，且该节点的左右子树还有空缺
            tree_node = self.my_queue[0]
            if tree_node.lchild == None: # 如果左儿子没有值，则插到左儿子处
                tree_node.lchild = node
                self.my_queue.append(tree_node.lchild)

            else:  # 左儿子有值，则插到右边
                tree_node.rchild = node
                self.my_queue.append(tree_node.rchild)

                # 注意，插入右儿子后，该节点的左右子树均已满，
                # 需要丢弃该节点（方便下次插入时找准位置）
                self.my_queue.pop(0)

    def pre_order(self, root):
        '''先序遍历， 递归法
        根节点-左节点-右节点'''
        if root == None:
            return

        print(root.value, end='  ')
        self.pre_order(root.lchild)
        self.pre_order(root.rchild)

    def in_order(self, root):
        ''' 中序遍历， 递归法（相当于层序输出）
        左节点-根节点-右节点
        '''
        if root == None:
            return

        self.in_order(root.lchild)
        print(root.value, end='  ')
        self.in_order(root.rchild)

    def after_order(self,root):
        '''后序遍历 递归实现
        左节点-右节点-根节点'''
        if root == None:
            return

        self.after_order(root.lchild)
        self.after_order(root.rchild)
        print(root.value, end='  ')

    def stack_pre_order(self, root):
        '''用堆栈实现先序遍历
         根节点-左节点-右节点

         从根节点开始，一直找他的左节点，把左节点存入堆栈
         直到最后一个左叶子节点（没有左子树了）

         出栈
        '''
        if root == None:
            return
        stack = [] #借助堆栈,堆栈存储的所有左节点
        node = root
        while node or stack:
            while node:  # 从根节点开始一直找他的左子树
                print(node.value, end='  ')
                stack.append(node)
                node = node.lchild  # 叶子节点的左右子树都是None，下一步会退出while循环
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            print([s.value for s in stack])
            if stack: # 栈非空，说明还有节点， 开始查看它的右子树
                node = stack.pop()
                node = node.rchild

    def stack_in_order(self, root):
        '''用堆栈实现中序遍历
        左节点-根节点-右节点
        
        从根节点遍历所有左节点
    
        然后
            弹出左叶子节点
            弹出左叶子节点的根节点、入栈右节点
            弹出左叶子节点的根节点的右节点
         '''
        if root == None:
            return

        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.lchild
                
            node = stack.pop()
            print(node.value, end='  ')
            node = node.rchild

    def stack_after_order(self, root):
        '''堆栈实现后序遍历，需两个堆栈
        '''
        while root == None:
            return

        stack1 = [root]
        stack2 = []  # 存储后序遍历的逆序

        while stack1: # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = stack1.pop()

            # 把当前节点的左节点、右节点都保存在stack1
            # # 先入栈、在栈里是先输出，但因为整体是逆序输出，所以这里是先输出
            if node.lchild:
                stack1.append(node.lchild)
            if node.rchild:
                stack1.append(node.rchild)
            # 把当前节点存储在stack2
            stack2.append(node)# 每次存储的都是stack1 的最后一个节点
            print('s1:',[s.value for s in stack1])
            print('s2:',[s.value for s in stack2])

        # 当stack1 为空的时候，已经遍历完所有元素，才输出stack2
        while stack2:  # 将myStack2中的元素出栈，即为后序遍历次序
            print(stack2.pop().value, end='  ')

    def queue_level(self,root):
        '''使用队列实现层序遍历'''
        if root == None:
            return 
        
        queue = [root] #可以利用列表实现队列
        while queue: # 逐层放入左右节点
            print([s.value for s in queue])
            node = queue.pop(0) # 每弹出一个根节点，都入栈两个子节点（如果有的话）
            # pop出第一个元素（如果不指定index=0，则默认最后一个元素）
            print(node.value, end='  ')
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)
            
        

def main():
    elems = range(10)
    tree = Tree()
    print(elems)
    print(tree)
    for elem in elems:
        tree.add(elem)
    print(tree)
    print(tree.root)
    print(tree.root.value)
    print(tree.root.lchild, tree.root.rchild)

    print('=====递归实现遍历=====')
    print("\n先序遍历")
    tree.pre_order(tree.root)
    print('\n中序遍历')
    tree.in_order(tree.root)
    print('\n后序遍历')
    tree.after_order(tree.root)
    
    print()
    print("====堆栈实现遍历====")
    print('先序遍历')
    tree.stack_pre_order(tree.root)
    print('中序遍历')
    tree.stack_in_order(tree.root)
    print('后序遍历')
    tree.stack_after_order(tree.root)
    print()

    print("====队列实现层序遍历====")
    tree.queue_level(tree.root)

    print('另一种树的初始化方法-只是用Node')
    root = Node('D',
                Node('B', Node('A'), Node('C')),
                Node('E', rchild=Node('G', Node('F'))))
    # 结果如图：https://images2017.cnblogs.com/blog/1178598/201708/1178598-20170813143038148-122262926.png
    # 见博客：https://www.cnblogs.com/freeman818/p/7252041.html
    print(root)
if __name__ == '__main__':
    main()
