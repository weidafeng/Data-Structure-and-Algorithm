# 给定两个字符串s1， s2
# s1 可以通过删除某些字符，得到s2，则说明s2是s1的子序列

# 注意，s1不能改变顺序
# eg： s1 = 'abcde', s2= 'ace' 是
# s2 = 'cab' 不是

def is_substring(s1, s2):
    start = 0
    for i in s2:
        for j in range(start, len(s1)):
            if i == s1[j]:
                start = j + 1
                break
            else:
                start = -1 # 如果s1 中不含有s2的某个字符，则标记位start=-1，return False
        print(start)
        if start == -1:
            return False
    return True

s1 = 'abcdehjab'
s2 = 'ab'

print(is_substring(s1,s2))

# 代码精简 双指针

def is_sub2(s1, s2):
    m = len(s1)
    n = len(s2)
    i, j = 0,0
    while i < m and j < n:
        if s1[i] == s2[j]:
            j += 1
        i += 1
    return j == n # j==n  说明s2 已经遍历完
print(is_sub2(s1,s2))