"""
EASY
https://leetcode.com/problems/valid-palindrome-ii/

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


def valid_palindrome(s: str) -> bool:
    if len(s) <= 2:
        return True

    def check_head_and_tail(s: str, has_already_error: bool = False) -> bool:
        if len(s) == 1:
            return True

        if len(s) == 2:
            if s[0] != s[1]:
                return not has_already_error
            else:
                return True

        if s[0] == s[-1]:
            return check_head_and_tail(s[1:-1], has_already_error)
        else:
            if has_already_error:
                return False
            else:
                return check_head_and_tail(s[0:-1], True) or check_head_and_tail(s[1:], True)

    return check_head_and_tail(s)
