# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         字符串匹配kmp算法.py
# Author:       wdf
# Date:         12/15/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
# -------------------------------------------------------------------------------

# TODO 自己写一遍
'''
KMP算法：
它利用之前已经部分匹配这个有效信息，保持主串的索引 i 不回溯，通过修改模式串的索引 j 的位置，让模式串尽量地移动到有效的位置。

视频讲解原理： https://www.bilibili.com/video/av11866460/
视频讲解c代码： https://www.bilibili.com/video/av16828557/

代码来自：https://github.com/TheAlgorithms/Python/blob/master/strings/knuth_morris_pratt.py
'''


def kmp(pattern, text):
    """
    The Knuth-Morris-Pratt Algorithm for finding a pattern within a piece of text
    with complexity O(n + m)
    1) Preprocess pattern to identify any suffixes that are identical to prefixes
        This tells us where to continue from if we get a mismatch between a character in our pattern
        and the text.
    2) Step through the text one character at a time and compare it to a character in the pattern
        updating our location within the pattern if necessary
    """

    # 1) Construct the failure array
    failure = get_failure_array(pattern)

    # 2) Step through text searching for pattern
    i, j = 0, 0  # index into text, pattern
    while i < len(text):
        if pattern[j] == text[i]:
            if j == (len(pattern) - 1):
                return True
            j += 1

        # if this is a prefix in our pattern
        # just go back far enough to continue
        elif j > 0:
            j = failure[j - 1]
            continue
        i += 1
    return False


def get_failure_array(pattern):
    """
    Calculates the new index we should go to if we fail a comparison
    :param pattern:
    :return:
    """
    failure = [0]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = failure[i - 1]
            continue
        j += 1
        failure.append(i)
    return failure


if __name__ == "__main__":
    # Test 1)
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert kmp(pattern, text1) and not kmp(pattern, text2)

    # Test 2)
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert kmp(pattern, text)

    # Test 3)
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert kmp(pattern, text)

    # Test 4)
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert kmp(pattern, text)

    # Test 5)
    pattern = "aabaabaaa"
    assert get_failure_array(pattern) == [0, 1, 0, 1, 2, 3, 4, 5, 2]
