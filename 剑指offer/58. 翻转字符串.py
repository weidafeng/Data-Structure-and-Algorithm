# 翻转字符串
# 输入一个英文句子,翻转句子中单词的顺序,但单词内的字符顺序不变
# 示例:
# I am a student.
# student. a am I

# 方法一, 先分割得到每个单词,然后单词列表逆序输出
def reverse_sting(s):
    return ' '.join(s.split(' ')[::-1])


# 方法二,手动实现
# 经典的两次旋转字符串
# 第一次,旋转整个字符串
# 第二次,旋转每个单词
def reverse_sting_2(s):
    # 第一次,旋转整个字符串
    s = reverse(s, 0, len(s)-1)
    # 第二次,旋转每个单词
    start, end = 0, 1
    while start < len(s) and end < len(s):
        # print(start, end, s)
        if s[end] == ' ':  # 空格,分隔单词
            s = reverse(s, start, end-1)
            start = end + 1  # 往后移动(移动到空格之后)
            end = start + 1
        else:
            end += 1

    return s

def reverse(s, start, end):
    '''旋转字符串s的从start到end区间的字符串, in-place'''
    if start >= end:  # 单个字符,无需交换
        return s
    ## 注意,Python中,字符串是不可交换类型,即无法直接修改字符串的某一个字符
    ## 因此类似        s[start], s[end] = s[end], s[start]
    ## 的语句会报错:   TypeError: 'str' object does not support item assignment

    # 可以借助列表实现
    s = list(s)
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    return ''.join(s)

def main():
    s = 'I am a student.'
    print(reverse_sting(s))


    # print(reverse('abcdefg', 0, 6))



    print(reverse_sting_2(s))






if __name__ == '__main__':
    main()