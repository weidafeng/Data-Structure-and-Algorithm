# 56-2. 数组中唯一只出现一次的数字
# 只有一个数字只出现了一次,其余所有数字都出现了3次

# 方法一, hash set 计数
# 方法二, 排序\遍历

# 方法三, 位运算
# 按二进制位进行累加
# 其他数都出现了三次,那么对应二进制位的和能被3整除
# 只有那个单个数字对应的二进制位不能被3整除

def find_only_once(lst):
    # 　int整形占32位
    bit_sum = [0 for _ in range(32)]  # 初始化一个32位的数组,存储每一个二进制位的和

    # 遍历每个数字
    for i in range(len(lst)):
        bit_mask = 1
        # 累计每个二进制位的和
        for j in range(31, -1, -1):
            bit = bit_mask & lst[i]  # 查看该整数在这一个二进制位(0 或 2 的n次方)
            if bit != 0:
                bit_sum[j] += 1
            bit_mask <<= 1

    # 得到结果(把二进制转换成十进制)
    # 逐个读取bit_sum数组里的每个二进制位
    print(bit_sum)
    result = 0
    for i in range(32):
        result = result << 1
        result += bit_sum[i] % 3  # 取余操作, 如果不能被3整除,说明是那个独特的数字,且余数正是那个数字的二进制大小

    return result

def main():
    lst = [1,1,1,2,3,3,3,4,4,4]
    print(find_only_once(lst))


if __name__ == '__main__':
    main()
