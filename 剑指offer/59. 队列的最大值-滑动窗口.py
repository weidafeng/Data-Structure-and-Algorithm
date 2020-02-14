# -*- coding: utf-8 -*-
# 59 队列的最大值
# 输入一个数组和窗口大小，给出当前窗口内的最大值
# 如
#     lst = [2, 3, 4, 2, 6, 2, 5, 1]  窗口 3
# 输出 [4, 6, 6, 6, 5]

# 思路： 队列，存储当前窗口内的最大值，以及索引（用来判断是否越界）


def max_in_windows(lst, k):
    queue = []  # 队列，存储当前窗口的最大值, 和他的索引
    res = []  # 存储结果
    for i, v in enumerate(lst):
        if not queue or i < k:  # 窗口还没满， 则逐个遍历、入队
            queue.append([i, v])
            if v > queue[0][1]:  # 如果新入队的元素比之前的元素大，则之前的元素不可能是最大值，出队
                queue.pop(0)
        else:  # 窗口已满
            # 如果越界，则去除旧元素
            if i - queue[0][0] > k - 1:
                queue.pop(0)

            # 如果新元素没有上一个元素大， 也可能是后面的最大值
            if v < queue[-1][1]:
                queue.append([i, v])
            else:  # 如果新元素比之前的元素更大，则替换
                while queue and v > queue[-1][1]:
                    queue.pop()
                queue.append([i, v])

            res.append(queue[0][1])
        print(i, v, queue, queue[0][1])
    return res

def main():
    lst = [2, 3, 4, 2, 6, 2, 5, 1]
    print(max_in_windows(lst, 3))


if __name__ == '__main__':
    main()
