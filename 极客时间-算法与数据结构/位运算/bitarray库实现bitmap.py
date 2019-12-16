# bitarray库实现bitmap.py
'''
install:
pip install bitarray

manual:
https://pypi.org/project/bitarray/

'''

from bitarray import bitarray
class Bitmap(object):
	def __init__(self, size):
		self.array = bitarray(size+1) # 调用库实现bitarray
		self.array.setall(0) # 初始化为0

	def set(self, index):
		self.array[index] = 1

	def test(self, index):
		return self.array[index]

	def tolist(self): # 打印
		return self.array.tolist()

	def to01(self): # 打印
		return self.array.to01()

# 使用bitmap对不重复的数组排序
def bitmap_sort(lst):
	size = max(lst)
	bitmap = Bitmap(size)
	print(bitmap.to01())

	for num in lst:
		bitmap.set(num)

	result = []
	for i in range(size + 1):
		if bitmap.test(i):
			result.append(i)
	print(bitmap.to01())
	print("原始数组：", lst)
	print("排序数组：", result)

def main():

	lst = [45, 2, 78, 35, 67, 90, 879, 0, 340, 123, 46]
	bitmap_sort(lst)


if __name__ == '__main__':
	main()
