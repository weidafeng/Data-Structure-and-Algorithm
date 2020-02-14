# 0~n-1中缺失的数字
# 一个长度为n-1的递增有序数组中所有数字都在0~n-1范围内,在该范围内的n个数字中,有去且仅有一个数字不在该数组中,找出来
# 如 [0,1,2,3,5,6,7], 范围在0-7的7个数字(本应该是8个数)中丢失了一个4


# 方法一, 0-n的所有数字累加,高斯公式求和,再减去数组中的每个数
# O(N)
def get_missing_digit(lst):
    n = lst[-1]
    total_sum = n * (n + 1) // 2
    return total_sum - sum(lst)

# 上面的方法没有利用数组有序这一特性
# 方法二
# 假设丢失的数字为m,
# 那么m之前,所有元素与其下标都相等; m之后元素与下表都不相等(下标比值小1)
# 也就是说m是第一个值与下标不相等的数字
#
# 使用二分法, 找到第一个下标与值不相等的元素
# O(log N)
def get_missing_digit_2(lst):
    start, end = 0, len(lst)-1

    # 二分查找
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == mid:  # 说明到该元素为止,前半段都不缺
            start = mid + 1  # 往后半段寻找
        elif lst[mid] > mid:  #  如果不相等,说明在此之前(含此位置),已经出现了缺失
            if mid == 0 or  (mid > 0 and lst[mid - 1] == mid - 1):  # 就是当前位置出现了缺失
                return mid
            else:
                end = mid - 1

    # 缺失的是最后一个
    if end == len(lst):
        return end

    # 边界条件, 不缺失
    return None




def main():
    lst = [0,1,2,3,5,6,7]
    print(get_missing_digit(lst))
    print(get_missing_digit_2(lst))


if __name__ == '__main__':
    main()