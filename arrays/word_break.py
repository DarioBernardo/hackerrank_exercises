"""
MEDIUM (for me HARD)
https://www.programcreek.com/2012/12/leetcode-solution-word-break/
https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented
into a space-separated sequence of one or more dictionary words.

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
from typing import List


def word_break(s: str, word_dict: List):
    pos = [-1]*(len(s) + 1)

    pos[0] = 0

    for i in range(0, len(s)):
        if pos[i] != -1:
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if sub in word_dict:
                    pos[j] = i

    return pos[len(s)] != -1

test_cases = [
    # ("leetcode", ["leet", "code"]),
    # ("applepenapple", ["apple", "pen"]),
    # ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
    # (
    # "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    # ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]),
    ("aaaaaaaaaabaaaaaa", ["a", "aa", "aaa", "aaaa"])
]


solutions = [
    # True,
    # True,
    # False,
    False,
    False
]

for test, sol in zip(test_cases, solutions):
    span = word_break(test[0], test[1])
    print(span)
    print(sol)
    assert span == sol
    print()

print("Done!")