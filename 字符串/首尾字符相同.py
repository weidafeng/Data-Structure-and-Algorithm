# 找到连续的字符串，要求其首尾字符相同

def get_same_substring(string):
    result = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i] == string[j] :
                print(string[i:j+1])
                result += 1
    return result
string = 'abcab'
print(get_same_substring(string))


# 数学解法
# a —— 1
# aa —— 3
# aaa —— 6
# aaaa —— 10

# 统计每个字母出现的次数n，满足要求的一共 n×（n+1）/2
from collections import Counter
def math_solver(string):
    count = Counter(string)
    result = 0
    for x in count:
        result += count[x] * (count[x]+ 1) //2
    return result
print(math_solver(string))