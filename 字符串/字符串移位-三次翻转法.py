# 将字符串s 移位d个单位

# 如 abcdefg， 移位2个单位
# 结果： cdefgab

# 方法： 三段翻转法
# abcdefg
#1、2. ba gfedc
#3.  cdefgab

def rotate(s, d):
    # round 1
    s = list(s)
    for i in range(0, d//2):
        s[i], s[d-i-1] = s[d-i-1], s[i]
    print(s)

    # round2
    for i in range((len(s)-d)//2):
        s[d+i], s[len(s)-i -1] = s[len(s)-i-1], s[d+i]
    print(s)

    # round3
    for i in range(0, len(s) // 2):
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
    print(s)
    print("".join(s))


s = '1234567'
rotate(s,5)

######################
# 代码精简

def reverse(s, start, end):
    # 对s的start到end位进行翻转
    while start < end:
        s[start],s[end] = s[end], s[start]
        start += 1
        end -= 1

def rotate2(s, d):
    n = len(s)
    reverse(s, 0, d-1)
    print(s)
    reverse(s, d, n-1)
    print(s)
    reverse(s, 0, n-1)
    print(s)

rotate2(list(s),5)