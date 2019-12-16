# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         字符串匹配-rolling hash参考代码.py
# Author:       wdf
# Date:         12/14/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

import timeit


class RollingHash:
    '''A rolling hash for a window of constant length into a text,
        both specified at construction.
    '''
    adjust = ord("a") - 1
    alphabet = 26

    def __init__(self, text, size_word):
        '''Set up a rolling hash for a window of size_word into text.'''
        self.text = text
        if len(text) < size_word:
            self.hash = None
            return
        rk = 0
        for c in text[:size_word]:  # 初始化hash值（前size_word个字母）
            rk = rk * self.alphabet + ord(c) - self.adjust
        self.hash = rk
        self.pos = -1
        self.window_start = 0
        self.window_end = size_word
        self.multiplier = RollingHash.alphabet ** (size_word - 1)

    def move_window(self):
        '''Advance window by one position.'''
        if self.window_end < len(self.text):
            # remove left letter from hash value
            self.hash = \
                (self.hash - (ord(self.text[self.window_start]) - RollingHash.adjust) * self.multiplier)  \
                * RollingHash.alphabet \
                + ord(self.text[self.window_end]) \
                - RollingHash.adjust
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        '''Return current window text.'''
        return self.text[self.window_start:self.window_end]

    def match(self, other):
        '''Return position of next match, or none.'''
        roll = self.hash
        text = self.text
        # "local copies" may help or hinder readability and performance
        start = self.window_start
        end = self.window_end
        limit = len(self.text)
        result = None
        while end < limit:
            if self.pos < other.hash == roll \
                and other.text == text[start:end] \
                and self.pos < start:
                result = self.pos = start
                break;
            roll = (roll - (ord(text[start])
                            - RollingHash.adjust) * self.multiplier) \
                * RollingHash.alphabet \
                + ord(text[end]) - RollingHash.adjust
            start += 1
            end += 1
        self.window_start = start
        self.window_end = end
        return result


verbose = True

def rabin_karp(word, text):
    '''Print indexes of matches for word in text.'''
    if word == "" or text == "":
        return None
    size_word = len(word)
    if size_word > len(text):
        return None

    rolling_hash = RollingHash(text, size_word)
    word_hash = RollingHash(word, size_word)

    for i in range(len(text) - size_word + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                if verbose:
                    print(i)
            else:
                print(rolling_hash.window_text(), '<>', word, "at", i)
        rolling_hash.move_window()
    return 'Pattern length: ', size_word


def karp_rabin(word, text):
    '''Print indexes of matches for word in text.'''
    size_word = len(word)
    if not 0 < size_word <= len(text):
        return None

    rolling_hash = RollingHash(text, size_word)
    word_hash = RollingHash(word, size_word)

    while True:
        position = rolling_hash.match(word_hash)
        if position is None:
            return 'Pattern length: ', size_word
        if verbose:
            print(position)


if __name__ == '__main__':
    text = input("Text: ")
    word = input("Pattern: ")
    print(rabin_karp(word, text))
    print(karp_rabin(word, text))
    verbose = False
    glob = globals()
    # have a look at timeit.Timer.repeat() and autorange(), too
    print(timeit.timeit('results = rabin_karp(word, text)',
                        globals=glob, number=9999))
    print(timeit.timeit('results = karp_rabin(word, text)',
                        globals=glob, number=9999))
