# 同字母异序词
# 字母都相同，出现次序不一样
# abcd —— dcba

def solution1(s1, s2):
    # 先排序，再比较
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

def solution2(s1,s2):
    # 记录每个字母出现的次数
    from collections import Counter
    return Counter(s1) == Counter(s2)

def solution3(s1, s2):
    # 同上，手写counter
    if len(s1) != len(s2):
        return False

    NO_OF_CHARS = 256 # ASCII 形式，一共256个
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
    for i in s1:
        count1[ord(i)] += 1  # ord, 转化成assic形式，如A=65
    for i in s2:
        count2[ord(i)] += 1

    print(count1,'\n',count2)
    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return False
    return True

s1 = '12abc'
s2 = 'abc21'
# print(solution3(s1,s2))

def solution4(s1, s2):
    # 同上，重写
    if len(s1) != len(s2):
        return False

    dic1 = {}
    dic2 = {}

    for i in s1:
        try:
            if dic1[i]:
                dic1[i] += 1
        except:
            dic1[i] = 1

    for i in s2:
        try:
            if dic2[i]:
                dic2[i] += 1
        except:
            dic2[i] = 1
    print(dic1,'\n', dic2)
    print(dic1 == dic2)

solution4(s1,s2)