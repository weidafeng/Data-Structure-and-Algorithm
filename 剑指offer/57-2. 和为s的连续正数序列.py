# 和为s的连续正数序列
# 输入一个正数s,打印所有和为s的连续正数序列(至少含有两个数)
#　如ｓ　＝　１５
# 输出: 1-5   4-6   7-8
# 因为: 1+2+3+4+5  =  4+5+6  = 7+8
#

# 思路: 也是双指针,从前往后遍历
#　因为至少两个数，所以left要遍历到  (s + 1) / 2

def find_continusous_sequences(s):

    # 初始化
    left = 1
    right = 2

    end =  (s + 1) // 2

    cur_sum = left + right

    result = []

    while left < end:
        if cur_sum == s:
            result.append([left, right])

        # 如果和太大,则逐个减去左边的值(左边的值较小,右边的值较大,所以可能需要减很多次)
        while cur_sum > s and left < end:
            cur_sum -= left
            left += 1

            if cur_sum == s:
                result.append([left, right])

        # 和太小,则继续往右加
        right += 1
        cur_sum += right

    return result


def main():
    print(find_continusous_sequences(9))
    print(find_continusous_sequences(15))


if __name__ == '__main__':
    main()
