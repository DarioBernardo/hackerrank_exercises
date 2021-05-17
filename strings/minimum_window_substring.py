"""
https://leetcode.com/problems/minimum-window-substring/  (HARD)
Given two strings s and t, return the minimum window in s which will contain all the characters in t.
If there is no such window in s that covers all characters in t, return the empty string "".
Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.



Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Example 3:
Input: s = "acbdbaab", t = "aabd"
Output: ""

Constraints:
1 <= s.length, t.length <= 105
s and t consist of English letters.
"""


def check_complete(d):
    for k, c in d.items():
        if c > 0:
            return False

    return True


def min_window(s: str, t: str) -> str:

    if len(s) == 0 or len(t) == 0:
        return ""

    t_hash_representation = dict()
    for letter in t:
        counter = t_hash_representation.get(letter, 0)
        counter += 1
        t_hash_representation[letter] = counter

    end = 0
    letters_stack = []
    positions_stack = []
    min_len = len(s) + 10
    current_string = ""

    while end < len(s) or (check_complete(t_hash_representation) and len(letters_stack) > 0):
        if end < len(s) and s[end] in t_hash_representation:
            t_hash_representation[s[end]] -= 1

            letters_stack.append(s[end])
            positions_stack.append(end)

        while check_complete(t_hash_representation) and len(letters_stack) > 0:
            if min_len > positions_stack[-1] - positions_stack[0] + 1:
                min_len = positions_stack[-1] - positions_stack[0] + 1
                current_string = s[positions_stack[0]:positions_stack[-1] + 1]

            positions_stack.pop(0)
            letter_popped = letters_stack.pop(0)
            t_hash_representation[letter_popped] += 1

        end += 1

    return current_string


test_cases = [
    ("bba", "ab"),
    ("acbdbaab", "aabd")
]

solutions = [
    "ba",
    "dbaa"
]

for test, sol in zip(test_cases, solutions):
    span = min_window(test[0], test[1])
    print(span)
    print(sol)
    assert span == sol
    print()

print("Done!")
