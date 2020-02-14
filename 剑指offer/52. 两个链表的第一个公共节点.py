# 两个链表的第一个公共节点
# 如：
#     1   2   3   4   6   7
#             4   5   6   7
# 第一个公共节点是6


# 两个链表是单向链表,如果有公共节点,则这两个链表从某一点开始都指向同一个节点
# 考虑从后往前遍历, 找到最后一个相同的节点
# 但链表是单向的,只能从前往后
# 先入后出--堆栈



class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = Node()  # 链表初始化，只有一个头结点
        self.length = 0

    def add_first(self, data):
        '''从头添加元素'''
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1

    # 打印链表
    def print_lkst(self):
        node = self.head.next  # 不打印头结点
        # print("head: ",head_node, head_node.data)
        while node != None:
            print(node.val, end=' ')
            node = node.next
        print()

# 方法一, 借助两个堆栈,存储两个链表的各个节点
def get_first_common_node(ls_1, ls_2):
    stack_1, stack_2 = [], []

    if ls_1 is None or ls_2 is None:
        return

    # 存储每个元素
    while ls_1:
        stack_1.append(ls_1.val)
        ls_1 = ls_1.next

    while ls_2:
        stack_2.append(ls_2.val)
        ls_2 = ls_2.next

    # 从后往前遍历(弹出),找出最后一个相同的元素
    res = None
    while True:
        node_1 = stack_1.pop()
        node_2 = stack_2.pop()

        if node_1 == node_2:
            res = node_1
        else:
            break
    return res


# 方法二
# 上面那个方法中,需要用到两个辅助栈
# 考虑到从公共节点之后,两个链表元素完全一样,那么不一样的都在链表最前面
# 可以先分别遍历两个链表,得到节点个数
# 长链表先走几步,然后两个链表同步开始,找到第一个公共节点
def get_first_common_node_2(ls_1, ls_2):
    length_1 , length_2 = 0, 0

    if ls_1 is None or ls_2 is None:
        return

    tmp_head_1 = ls_1  # 备份头结点,因为后面还要用
    tmp_head_2 = ls_2

    # 存储每个元素
    while ls_1:
        ls_1 = ls_1.next
        length_1 += 1
    while ls_2:
        ls_2 = ls_2.next
        length_2 += 1

    ls_1, ls_2 = tmp_head_1, tmp_head_2  # 恢复头结点
    # 假设第一个链表更长
    if length_2 > length_1:
        ls_1, ls_2 = ls_2, ls_1
        length_1, length_2 = length_2, length_1

    length_diff = length_1 - length_2

    # 长链表先走几步
    while length_diff:
        ls_1 = ls_1.next
        length_diff -= 1

    # 然后同时遍历,找到第一个公共节点
    while ls_1.val != ls_2.val:
        ls_1 = ls_1.next
        ls_2 = ls_2.next

    return ls_1.val





def main():
    # 新建一个链表
    print("新建一个链表")
    l_1 = LinkedList()
    for i in [7,6,3,2,1]:
        l_1.add_first(i)
    l_1.print_lkst()
    print()

    l_2 = LinkedList()
    for i in [7,6,5,4]:
        l_2.add_first(i)
    l_2.print_lkst()

    print('第一个公共节点-方法一')
    print(get_first_common_node(l_1.head, l_2.head))

    print('第一个公共节点-方法二')
    print(get_first_common_node_2(l_1.head, l_2.head))


if __name__ == '__main__':
    main()
