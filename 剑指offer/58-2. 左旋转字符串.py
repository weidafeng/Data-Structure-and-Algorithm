# 58-2. 左旋转字符串
#  把字符串前面的若干个字符转移到字符串尾部
# 示例：
# 输入 abcdefg  数字2
# 输出 cdefgab


# 思路，同样旋转两次
# 两部分分别旋转 ba  gfedc
# 整个旋转      cdefgab

def rotate_at_position(s, n):
    left, right = s[:n], s[n:]
    print(left, right)

    # 第一次，两部分分别旋转
    left = reverse(left, 0, len(left) - 1)
    right = reverse(right, 0, len(right) - 1)

    # 第二次，旋转整个字符串
    return reverse(left+right, 0, len(s)-1)


def reverse(s, start, end):
    if start >= end:
        return s

    s = list(s)  # 借助数组实现交换
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    return ''.join(s)

def main():
    print('测试reverse函数')
    s = 'abcdefg'
    print(reverse(s, 0, len(s)-1))

    print('测试旋转函数')
    print(rotate_at_position(s, 2))


if __name__ == '__main__':
    main()