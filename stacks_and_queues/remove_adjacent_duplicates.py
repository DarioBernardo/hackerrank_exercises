"""
EASY
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Remove All Adjacent Duplicates In String:

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.


Example 1:

Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
"""


def remove_duplicates(s: str) -> str:

    if len(s) <= 1:
        return s

    stack = []

    for c in s:

        if len(stack) > 0 and stack[-1] == c:
            _ = stack.pop()

        else:
            stack.append(c)


    return "".join(stack)

din = [
    "abbaca",
    "aabbaca",
    # "aaabbca"
]

dout = [
    "ca",
    "aca",
    # "ca"
]


for data_in, expected_result in zip(din, dout):
    actual_result = remove_duplicates(data_in)
    print(f"Expected: {expected_result}   Actual: {actual_result}")
    assert expected_result == actual_result
