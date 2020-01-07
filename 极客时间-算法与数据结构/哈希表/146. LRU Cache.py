# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         146. LRU Cache.py
# Author:       wdf
# Date:         1/7/2020
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------


# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

# Runtime: 204 ms, faster than 63.24% of Python3 online submissions for LRU Cache.
# Memory Usage: 22.1 MB, less than 22.73% of Python3 online submissions for LRU Cache.

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_queue = OrderedDict()
        self.capacity = capacity
        self.size = 0

    # get(key) - Get the value (will always be positive) of the key if the key
    # exists in the cache, otherwise return -1.
    def get(self, key: int) -> int:
        if key in self.cache_queue:
            value = self.cache_queue.pop(key)
            self.cache_queue[key] = value # 也可以替换为self.cache_queue.move_to_end(key)
            return value
        else:
            return -1

    # put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
    def put(self, key: int, value: int) -> None:
        # 先看缓存里面是否存在
        if key in self.cache_queue:
            self.cache_queue.pop(key)
        elif self.size >= self.capacity:  # 容量满了，弹出最后一个元素
            self.cache_queue.popitem(last=False)
        else: # 即不在缓存里，又没有满——直接放
            # 容量没满
            self.size += 1
        self.cache_queue[key] = value



def main():
    # Your LRUCache object will be instantiated and called as such:
    capacity = 3
    dic = {'key1':'value1', 'k2':'v2','k3':'v3'}
    obj = LRUCache(capacity)
    key = 'key1'
    value = 'value1'
    param_1 = obj.get(key)
    obj.put(key,value)


if __name__ == '__main__':
    main()