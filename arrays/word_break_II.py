"""
HARD (for me VERY HARD)
https://www.programcreek.com/2014/03/leetcode-word-break-ii-java/
https://leetcode.com/problems/word-break-ii/

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence
where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]


Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.


Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
"""
from typing import List


def word_break_ii(s: str, word_dict: List):

    if len(s) == 0 or len(word_dict) == 0:
        return []

    pointer = 1
    solution = []
    while pointer <= len(s):
        sub = s[0:pointer]
        if sub in word_dict:
            if len(s[pointer:]) > 0:
                list_of_breakdowns = word_break_ii(s[pointer:], word_dict)
                for elem in list_of_breakdowns:
                    solution.append(f"{sub} {elem}")
            else:
                solution.append(f"{sub}")

        pointer += 1

    return solution


test_cases = [
    ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),
    ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"])
]

solutions = [
    ["cats and dog", "cat sand dog"],
    ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
    []
]

for test, sol in zip(test_cases, solutions):
    span = word_break_ii(test[0], test[1])
    print(span)
    print(sol)
    assert sorted(span) == sorted(sol)
    print()

print("Done!")
