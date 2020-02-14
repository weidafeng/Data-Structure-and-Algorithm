# 在有序数组中统计某个数字出现的次数
# 如: [1,2,3,3,3,3,4,4,5], 3出现了4次

# 方法一,暴力统计
def counts_of_digit(lst, target):
    if not lst:
        return None

    count = 0
    # 先找到目标数字
    for i in range(len(lst)):
        if lst[i] > target:  # 越界了, 可以提前终止
            return count
        elif lst[i] < target:
            continue
        else:  # 相等
            count += 1
    return count


# 方法二,充分利用数组是有序的条件 -- 二分查找
def counts_of_digit_2(lst, target):

    def get_first(lst, target, start, end):
        # 使用二分查找,找到第一个target的索引

        # 递归终止条件
        if start > end:
            return

        mid = (start + end) // 2
        mid_data = lst[mid]
        if mid_data == target:  # 如果是要找的数,则往前看
            if mid == 0 or (mid > 0 and target != lst[mid - 1]):
                return mid  # 是第一个target
            else:
                end = mid - 1
        elif mid_data < target:  # 在右边
            start = mid + 1
        else:   # 在左边
            end = mid - 1
        return get_first(lst, target, start, end)

    def get_last(lst, target, start, end):
        # 使用二分查找,找到最后一个target的索引
        if start > end:
            return

        mid = (start + end) // 2
        mid_data = lst[mid]
        if mid_data == target:
            if mid == len(lst) - 1 or (mid < len(lst) - 1 and  target != lst[mid + 1]):
                return mid  # 是最后一个target
            else:
                start = mid + 1
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        return get_last(lst, target, start, end)


    first = get_first(lst,target, 0, len(lst))
    last = get_last(lst,target, 0, len(lst))
    # print(first, last)
    return last - first + 1


# 方法三,使用bisect二分查找库
def counts_of_digit_3(lst, target):
    import bisect
    first = bisect.bisect_left(lst, target)
    last = bisect.bisect_right(lst, target)
    # print(first, last)
    return last - first  # 不在额外加一,因为bisect_right是在右边插入的位置,比最后一个元素所在的位置大一


def main():
    lst = [1,2,3,3,3,3,4,4,5]
    for i in set(lst):
        print(i, counts_of_digit(lst, i))

    print('*'* 10 )
    for i in set(lst):
        print(i, counts_of_digit_2(lst, i))

    print('*'* 10 )
    for i in set(lst):
        print(i, counts_of_digit_3(lst, i))


    # print('*' * 10)
    # print(counts_of_digit_3(lst, 3))

if __name__ == '__main__':
    main()