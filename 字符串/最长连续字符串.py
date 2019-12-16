# 找到字符串中最长的连续字符串

def get_longest_string(string):
    global_count = 1
    local_count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            local_count += 1
            global_count = max(local_count, global_count)
        else:
            local_count = 1
    return global_count

s = 'abcaaabcdaaaad'
print(get_longest_string(s))