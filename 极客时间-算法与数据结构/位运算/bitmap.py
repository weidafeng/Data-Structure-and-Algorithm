# bitmap.py
# 用bitmap算法实现【无重复整数】的排序
'''
教程（特别详细）：
https://my.oschina.net/goal/blog/200347
'''
# bitmap通常基于数组实现，数组中的每个元素可以看成一系列二进制数
# int整形元素，可以看做31位二进制数
# 数组中的各个元素又组成一个更大的二进制集合

# 对于python的32位int整形来说，默认为有符号类型，最高位为符号位，所以
# 可以表示31个二进制位

# eg： 包含4个元素的int数组，一共4*31=124个二进制位
# 如果要在第90个二进制位上操作，则需要
# 1）现找到他在哪个元素
# 2）再找到他在该元素的哪个二进制位
# 3）执行操作

import math
class Bitmap(object):
	def __init__(self, max_number):
		'''eg， 对于90来说，因为单个整形只能使用31位，所以要保存90，需要3个int元素'''
		self.size = math.ceil(max_number/31) # 向上取整，保证所有元素都装得下
		self.array = [0 for _ in range(self.size)] # 初始化bitmap

	def cal_element_index(self, num, up=False):
		'''计算当前元素在数组中是第几位'''
		if up: # 向上取整
			return math.ceil(num / 31) # 向上取整，计算最多需要多少个int元素
		return num // 31 # 不需要向上取整（ 数组索引是从0开始

	def cal_bit_index(self, num):
		'''计算该值在数组元素中的第几个二进制位'''
		return num % 31


	def set_1(self, num):
		'''输入值num， 把他放到指定二进制位（该位置一）'''
		elem_index = self.cal_element_index(num) # 第几个数组元素
		bit_index = self.cal_bit_index(num)  # 该数组元素上的第几个二进制位

		element = self.array[elem_index]   # 先取出所在的数组元素
		self.array[elem_index] = element | (1 << bit_index) # 位运算， 置一
		# 具体步骤： 先通过左移，找到需要置一的那一位
		# 再通过或运算，置一（不会修改其他位的值，其他位之前为1，与0或之后，还是1，之前为0，与0或之后还是0）

	def clear(self, num):
		'''输入值num，将对应的二进制位清零'''
		elem_index = self.cal_element_index(num) # 第几个数组元素
		bit_index = self.cal_bit_index(num)  # 该数组元素上的第几个二进制位

		element = self.array[elem_index]   # 先取出所在的数组元素
		self.array[elem_index] = element & (~(1 << bit_index)) # 位运算，清零
		# 向左移位，找到要操作的二进制位 00000010000
		# 取反， 11111111011111
		# 与运算，只有那一位会变成0， 其他位不会改变

	def test_1(self, num)->bool:
		'''测试某一位是否为1（用于输出）'''
		elem_index = self.cal_element_index(num)
		bit_index = self.cal_bit_index(num)
		
		return self.array[elem_index] & (1 << bit_index)




# 实现一个无重复数组的排序
def bitmap_sort(lst, MAX=879):
	MAX = MAX # 已知待排序数组的最大元素
	result = []
	bitmap = Bitmap(MAX)
	for num in lst: # 把待排序的每个元素都放入bitmap
		bitmap.set_1(num)

	for i in range(MAX + 1): # 遍历bitmap的所有元素，判断是否有值
		if bitmap.test_1(i): # 测试第i个二进制位是否有元素
			result.append(i) # 第i位有元素，说明i这个值存在
	print(bitmap.array)
	print("原始数组：", lst)
	print("排序数组：", result)


def main():
	bitmap = Bitmap(90)
	bitmap.set_1(11)
	print(bitmap.array)
	bitmap.set_1(32)
	print(bitmap.array)
	bitmap.set_1(0)
	print(bitmap.array)
	print(bitmap.test_1(0))
	bitmap.set_1(1)
	print(bitmap.test_1(1))
	print(bitmap.test_1(2))
	bitmap.clear(1)
	print(bitmap.test_1(1))

	print()
	lst = [45, 2, 78, 35, 67, 90, 879, 0, 340, 123, 46]
	bitmap_sort(lst)


if __name__ == '__main__':
	main()