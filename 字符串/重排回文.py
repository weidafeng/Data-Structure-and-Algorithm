# 对一个字符串进行重排，是否存在回文

# 如：aabccdd —— acdbdca 是
# 如： abc 不是

# 思路：
# 如果s长度为偶数，则每个字母必须出现偶数次
# 如果长度为奇数，只有一个字母出现奇数次

from collections import Counter

def is_permucate_palindrome(s):
    n = len(s)
    count = Counter(s)
    odd = 0
    for c in count.values():
        if n%2 and odd >=2: # 奇数
            return False
        if n%2 == 0: # 偶数
            if odd:
                return False
        if c % 2:
            odd += 1
    return True



print(is_permucate_palindrome('abcac'))