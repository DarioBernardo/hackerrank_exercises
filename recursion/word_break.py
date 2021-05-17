"""
EASY
https://leetcode.com/explore/interview/card/facebook/55/dynamic-programming-3/3036/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

"""
from functools import lru_cache
from typing import List, FrozenSet


def wordBreak(s: str, wordDict: List[str]) -> bool:

    @lru_cache()
    def wordBreakMemo(s: str, wordDict: FrozenSet[str]) -> bool:

        if len(wordDict) == 0:
            return False

        if len(s) == 0:
            return True

        pointer = 1
        is_valid = False
        while pointer < len(s) + 1:
            sub = s[0:pointer]
            if sub in wordDict:
                is_valid = wordBreakMemo(s[pointer:], wordDict)
                if is_valid:
                    return True

            pointer += 1

        return is_valid

    return wordBreakMemo(s, frozenset(wordDict))


din = [
    ("leetcode", ["leet", "code"]),
    ("applepenapple", ["apple", "pen"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
    ("ccbb", ["bc", "cb"]),
    ("a", ["b"])
]

dout = [
    True,
    True,
    False,
    False
]

for data_in, expected_result in zip(din, dout):
    actual_result = wordBreak(data_in[0], data_in[1])
    print(f"Expected: {expected_result}   Actual: {actual_result}")
    assert expected_result == actual_result


