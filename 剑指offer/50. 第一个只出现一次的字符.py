# 字符串中第一个只出现依次的字符。
# 如字符串 ‘abaccdeff’中，输出b

# 思路： 遍历两次，第一次hash set 计数，第二次遍历输出第一个次数为1的字符

def first_once_char(s):
    count = {}
    # 第一次遍历，计数
    for c in s:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    # 第二次遍历，查找
    for c in s:
        if count[c] == 1:
            return c
    # 异常
    return None


def main():
    s = 'abaccdeff'
    print(first_once_char(s))

if __name__ == '__main__':
    main()
