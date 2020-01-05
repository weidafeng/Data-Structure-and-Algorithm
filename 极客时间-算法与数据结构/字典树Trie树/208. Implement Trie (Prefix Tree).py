# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         208. Implement Trie (Prefix Tree).py
# Author:       wdf
# Date:         1/2/2020
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
# -------------------------------------------------------------------------------

# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
# Note:
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.


# Success
# Details
# Runtime: 124 ms, faster than 95.25% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 26.3 MB, less than 66.67% of Python3 online submissions for Implement Trie (Prefix Tree).

class Trie_2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = -1

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        # 得到的结果存储在root里，是一个嵌套的字典结构
        """
        curNode = self.root
        for c in word:
            if not c in curNode:  #如果该字符是个新字符，需要新开一个子树
                curNode[c] = {}
            curNode = curNode[c] # 如果该字符之前出现过，则跳转到该子树，从该子树开始
        curNode[self.end] = True # 遍历完字符串，给每个字符串添加一个结束标识符

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for c in word:
            if not c in curNode:   # 如果不存在该字符，则直接返回false
                return False
            curNode = curNode[c]  # 如果该字符存在，则跳转到该字符、遍历下一个

        # 即便该字符串所有字符都存在，但也不一定是一个完整的子串（可能只是公共前缀）
        # Doesn't end here
        if not self.end in curNode:
            return False

        # 所有字符串都存在，且是个完整的字符串（不只是公共前缀）
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for c in prefix:
            if not c in curNode:
                return False
            curNode = curNode[c]

        # 与search相比，不需要判断是否有结束标识符
        return True

    def print_trie(self):
        print(self.root)


## 代码精简
# Success
# Details
# Runtime: 128 ms, faster than 91.38% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 26.1 MB, less than 66.67% of Python3 online submissions for Implement Trie (Prefix Tree).
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_word = "#"  # 标记字符串结束

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        # 得到的结果存储在root里，是一个嵌套的字典结构

        """
        node = self.root

        for c in word:
            node = node.setdefault(c, {})
            # 如果字符c存在的话，返回c;
            # 如果不存在，则开辟为一个新的空字典
            # 然后返回字典c或者空字典（相当于调整到下一层字典），

        node[self.end_word] = True  # 插入每个单词后，该单词最后一个字符都设置为True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]

        return self.end_word in node  # 精简

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]

        return True

    def print_trie(self):
        print(self.root)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


def main():
    word = 'word'
    obj = Trie()
    print(obj)
    obj.insert(word)
    obj.print_trie()

    print(obj.search('word'))
    print(obj.search('world'))
    print(obj.search('wor'))

    print(obj.startsWith('wor'))
    print(obj.startsWith('word'))
    print(obj.startsWith('world'))

    obj.insert('world')
    obj.print_trie()

    obj.insert('abc')
    obj.print_trie()


if __name__ == '__main__':
    res = {'w':
               {'o':
                    {'r':
                         {'d':
                              {-1: True},
                          'l':
                              {'d':
                                   {-1: True}}}}},
           'a':
               {'b':
                    {'c':
                         {-1: True}}}}
    main()
