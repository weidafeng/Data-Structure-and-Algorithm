# 判断一个数字是否为回文（不允许转化为字符串）

# 依次比较最高位和最低位是否相等
# 若相等，则去掉最高位、最低位，继续比较

def int_palindrome(x):

    ranger = 1
    while x // ranger >= 10: # 找到最高位的进制
        ranger *= 10

    while x:
        print(x)
        low = x % 10
        high = x // ranger
        if low != high:
            return False
        x = (x % ranger) // 10
        ranger //= 100
    return True

int_palindrome(123454321)