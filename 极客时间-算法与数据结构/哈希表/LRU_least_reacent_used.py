# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         LRU_least_reacent_used.py
# Author:       wdf
# Date:         11/19/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
# -------------------------------------------------------------------------------

# orderdict 实现
# 两个功能，一个是往里装数据（缓存数据），一个是往外吐数据（命中缓存），所以我们的缓存对外只需要put和get两个接口就可以了。
'''
- 有新数据（意味着数据之前没有被缓存过）时，加入到列表头
- 缓存到达最大容量时，需要淘汰数据多出来的数据，此时淘汰列表尾部的数据
- 当缓存中有数据被命中，则将数据移动到列表头部（相当于新加入缓存）

按上面的逻辑我们可以看到，一个数据如果经常被访问就会不断地被移动到列表头部，不会被淘汰出缓存，而越不经常访问的数据，越容易被挤出缓存。

链接：https://juejin.im/post/5a9e6835f265da23937697ea

# OrderedDict是在普通字典的方法保证了插入的有序，正如它的名字一样，保存时按照它插入的顺序保存的。
OrderedDict 也是 dict 的子类，其最大特征是，它可以“维护”添加 key-value 对的顺序。
简单来说，就是先添加的 key-value 对排在前面，后添加的 key-value 对排在后面。

由于 OrderedDict 能维护 key-value 对的添加顺序，因此即使两个 OrderedDict 中的 key-value 对完全相同，
但只要它们的顺序不同，程序在判断它们是否相等时也依然会返回 false。

同时要强调的是这个类还有一个特殊的方法popitem(Last=False),
当Last参数为False时，说明其是以队列先进先出方式弹出第一个插入字典的键值对，
而当Last参数为True时，则是以堆栈方式弹出键值对。
'''
import collections

class LRUCache:
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.queue = collections.OrderedDict()

    def get(self, key):
        if key not in self.queue:
            return None  # 要找的数据不在缓存中返回 None
        value = self.queue.pop(key)  # 将命中缓存的数据移除
        self.queue[key] = value  # 将命中缓存的数据重新添加到头部
        return self.queue[key]

    def put(self, key, value):
        if key in self.queue:  # 如果已经在缓存中，则先移除老的数据
            self.queue.pop(key)
        elif len(self.queue.items()) == self.capacity: # 如果不在缓存中并且到达最大容量，则把最后的数据淘汰
            self.queue.popitem(last=False) # Last参数为False时，说明其是以队列先进先出方式弹出第一个插入字典的键值对，
            # The pairs are returned in LIFO order if last is true or FIFO order if false.
        self.queue[key] = value  # 将新数据添加到头部


# 基于普通dict和list实现
'''借助于普通dict和list来实现，其实就是自己来实现一个OrdereDict，保证插入的有序（或说是借助列表来记录插入的顺序）'''
'''https://www.cnblogs.com/break-python/p/5459169.html'''
class LRUCache_list(object):
    def __init__(self, size=5):
        self.size = size
        self.cache = dict()
        self.key = []  # 记录dict的输入顺序（最新插入的，放在最前面）

    def get(self, key):
        if key in self.cache.keys(): # 如果缓存里存在该值
            # 调整顺序（删除旧的次序、重新插入到第一个）
            self.key.remove(key)  # list 删除该值
            self.key.insert(0, key) # list 重新插入该值（插在第一位，表示最新访问）
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        if key in self.cache.keys():  # 如果缓存里存在该值

            # 下面这两步可以不做，不需要先删除、再插入，因为cache是个字典，无序
            self.cache.pop(key)     # 先删除
            self.cache[key] = value  # 重新加入

            self.key.remove(key)     # 删除原值、重新插入（保证顺序）
            self.key.insert(0, key)
        elif len(self.cache) == self.size:  # 如果缓存里不存在，且缓存已满
            old_key = self.key.pop()    # 删除缓存里最后一个元素（先从顺序表里找到最后一个key）
            self.cache.pop(old_key)     # 缓存表根据key删除元素
            self.key.insert(0, key)     # 记录次序（最新）
            self.cache[key] = value     # 把最新的元素放入缓存表
        else:                           # 如果缓存没满、且缓存里没有该元素
            self.cache[key] = value     # 放入缓存
            self.key.insert(0, key)     # 记录次序（最新）

def main():
    test = LRUCache(3)
    test.put('a', 1)
    test.put('b', 2)
    test.put('c', 3)
    test.put('d', 4)
    test.put('e', 5)
    # test.set('f',6)
    print(test.get('a'))
    print(test.get('b'))
    print(test.get('c'))
    print(test.get('d'))
    print(test.get('e'))

    print("*"*20)
    test = LRUCache_list(3)
    test.put('a', 1)
    test.put('b', 2)
    test.put('c', 3)
    test.put('d', 4)
    test.put('e', 5)
    # test.set('f',6)
    print(test.get('a'))
    print(test.get('b'))
    print(test.get('c'))
    print(test.get('d'))
    print(test.get('e'))

if __name__ == '__main__':
    main()
