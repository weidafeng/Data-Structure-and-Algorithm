# 字符流中第一个只出现依次的字符。
# 如字符流 ‘google’中
# 输入    输出
# g         g
# go        g
# goo       g
# goog      None
# googl     l
# google    l


# 思路： 遍历，按出现顺序记录

count = {}  # 计数
res = []  # 存储结果
def first_once_char_in_stream(c):
    global count, res

    if c not in count:  # 之前没有出现过
        count[c] = 1  # 计数
        res.append(c)  # 记录当前结果
    else:  # 如果已经出现了
        res.remove(c)  # 清除结果
        count[c] += 1  # 计数

    # 输出
    if res:
        return res[0]
    else:
        return None


def main():

    s = 'google'
    for c in s:
        print(first_once_char_in_stream(c))

if __name__ == '__main__':
    main()
