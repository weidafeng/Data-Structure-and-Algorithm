# 删除字符串中所有重复的字符
# 如字符串 ‘google’中，输出gole

# 思路： 遍历一次，如果之前出现过，则不统计，如果未出现过，则添加

def delete_all_duplicate_char(s):
    count = {}
    res = ''
    # 第一次遍历，计数
    for c in s:
        if c not in count:
            res += c
            count[c] = True
    return res


# 方法二，自己手动实现一个hash set，因为输入的都是字符串，ascii码的区间只有26个
def delete_all_duplicate_char_2(s):
    count = [0 for _ in range(26)]
    res = ''

    # 第一次遍历，计数
    for c in s:
        if 'a' > c or 'z' < c:  # 限定输入的合法范围
            raise Exception('Wrong inputs!')
        if count[ord(c) - ord('a')] == 0:  # 如果之前没有出现过
            res += c
            count[ord(c) - ord('a')] = 1
    return res



def main():
    s = 'abaccdeff'
    print(delete_all_duplicate_char(s))
    print(delete_all_duplicate_char_2(s))

    s = 'google'
    print(delete_all_duplicate_char(s))
    print(delete_all_duplicate_char_2(s))

if __name__ == '__main__':
    main()
