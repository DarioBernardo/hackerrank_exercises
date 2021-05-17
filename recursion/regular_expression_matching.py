"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false
"""

# WRONG SOLUTION THIS DO NOT WORKS WELL


def is_match(s: str, p: str) -> bool:
    if not p:
        return not s

    if p == ".*":
        return True

    if len(s) == 0:
        if (len(p) == 2 and p[1] == '*') or len(p) == 0:
            return True
        return False

    """
    s = aab
    p = c*a*b


    len(s) = 3
    w = a
    same_letter_counter = 2

    """

    w = s[0]
    same_letter_counter = 1
    while same_letter_counter < len(s) and w == s[same_letter_counter]:
        same_letter_counter += 1

    first_match = p[0] in [w, "."]
    if not first_match:
        if len(p) > 1 and p[1] == "*":
            return is_match(s, p[2:])
        else:
            return False

    if (same_letter_counter > 1 and len(p) == 1) or (same_letter_counter > 1 and len(p) > 1 and p[1] != "*"):
        if first_match:
            return is_match(s[1:], p[1:])
        return False

    else:
        if first_match and (len(p) > 1 and p[1] != "*"):
            return is_match(s[same_letter_counter:], p[1:])
        return is_match(s[same_letter_counter:], p[2:])


din = [
    # ("mississippi", "mis*is*ip*.")
    ("aa", "aa")
]

expected_results = [
    True
]

for i, expected in zip(din, expected_results):
    actual = is_match(i[0], i[1])
    print(actual)
    print(expected)
    # assert actual == expected
