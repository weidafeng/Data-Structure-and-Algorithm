# 判断一个字符串是否为另一个字符串的移位
# 如 ABCD和BCDA

# 技巧：
# 把s1重复两次，判断s2 是否为s1的子串
# 如果是，则说明s2是s1的移位
# 如： ABCDABCD , BCDA 一定是其子串

def transplant(s1, s2):
    return s2 in (s1 + s1)

s1 = 'ABCD'
s2 = 'BCDA'

print(transplant(s1,s2))