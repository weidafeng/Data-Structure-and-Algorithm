# 从字符串s里任选k个字符，组成最长的回文字符串

# 为每个字符计数，偶数个的字符全留着，奇数个的字符只留一个


from collections import Counter

def longest_palindrome(s):
    count = Counter(s)
    odd = 0
    even = 0
    for c in count.values():
        if c%2 == 0: # 偶数
            even += c
        if c%2: #奇数
            if c > 2 :
                even += c-1 # 比如有3个c， 则可以取其中两个
            odd += 1

    return even + 1 if odd else even



print(longest_palindrome('abccccdd'))