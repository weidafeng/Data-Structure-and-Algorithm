# 判断一个字符串是否为“移位回文”
# 即，字符串s经过移位后，可以转化为回文形式
# eg： aab——aba 是回文
# eg： abc——bca、cab 均不是回文

# 思路：
# s+s（拼接两次），滑动窗口为len(s)

def is_palindrome(s):
    return s == s[::-1]


def is_tran_palindrome(s):
    n = len(s)
    s += s

    for i in range(n):
        print(s[i:i+n])
        if is_palindrome(s[i:i+n]):
            return True
    return False

s = 'aabda'
print(is_tran_palindrome(s))