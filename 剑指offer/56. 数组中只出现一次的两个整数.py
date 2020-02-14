# 数组中只出现一次的两个整数,其他整数都出现2次
# 方法:
# 先全部异或,最终结果一定是不一样的两个整数的异或,不为0(其他的出现两次,异或为0,都抵消了)

from functools import reduce

def find_numbers_appear_once(lst):
    xor_res = reduce(lambda a, b: a^b, lst)  # 两两异或

    # 找到异或结果中第一个1的位置
    n = 0
    while xor_res & 1 == 0:
        xor_res >>= 1
        n += 1

    # 根据第n为是否为1, 将列表中的元素分为两部分
    group_1 = []
    group_2 = []
    for val in lst:
        if val & (1<<n):
            group_1.append(val)
        else:
            group_2.append(val)
    print(group_1, group_2)
    return reduce(lambda a,b:a^b, group_1), reduce(lambda a,b: a^b, group_2)

# 精简
def find_numbers_appear_once_2(lst):
    xor_res = reduce(lambda a, b: a^b, lst)  # 两两异或

    # 找到异或结果中第一个1的位置
    n = 0
    while xor_res & 1 == 0:
        xor_res >>= 1
        n += 1

    # 根据第n为是否为1, 将列表中的元素分为两部分
    # 不需要使用两个列表存储各个部分,可以只保存异或结果
    res_1, res_2 = 0, 0
    for val in lst:
        if val & (1<<n):
            res_1 ^= val
        else:
            res_2 ^= val
    return res_1, res_2


def main():
    lst = [2,4,3,6,3,2,5,5]
    print(find_numbers_appear_once(lst))
    print(find_numbers_appear_once_2(lst))

if __name__=='__main__':
    main()