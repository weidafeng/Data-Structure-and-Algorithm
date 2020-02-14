# 57. 和为s的数字
# 输入一个递增序列的数组, 和一个数字s, 在数组中查找两个数, 使得他们的和正好是s
# 如果有多对,输出一对即可

# 方法: 典型的双指针问题
def find_nums_with_sum(lst, target):
    left, right = 0, len(lst) - 1

    while left < right:
        if lst[left] + lst[right] == target:
            return lst[left], lst[right]
        elif lst[left] + lst[right] > target:
            right -= 1
        else:
            left += 1

    return None


def main():
    lst = [1,2,4,7,11,15]
    print(find_nums_with_sum(lst, 15))

    # 边界测试
    lst = [1,2,4,7,11,15]
    print(find_nums_with_sum(lst, 122))


    lst = [1,2,4,7,11,15]
    print(find_nums_with_sum(lst, 0))


    lst = []
    print(find_nums_with_sum(lst, 0))


if __name__ == '__main__':
    main()
