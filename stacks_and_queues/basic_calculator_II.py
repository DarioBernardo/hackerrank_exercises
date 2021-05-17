"""
https://leetcode.com/problems/basic-calculator-ii/ (MEDIUM)

Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


Example 1:
Input: s = "3+2*2"
Output: 7


Example 2:
Input: s = " 3/2 "
Output: 1


Example 3:
Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    def calculate(self, s: str) -> int:

        s = s.strip()

        is_negative = False
        if s[0] == "-":
            is_negative = True
            s = s[1:]

        s = list(s)
        digit = ""
        accumulator = 1
        operation = ""
        while len(s) > 0 and s[0] not in ["+", "-"]:
            if s[0] != " ":
                if s[0] in ["/", "*"]:
                    if operation != "":
                        if operation == "*":
                            accumulator *= int(digit)
                        elif operation == "/":
                            accumulator //= int(digit)
                    else:
                        accumulator = int(digit)

                    digit = ""
                    operation = s.pop(0)
                else:
                    digit += s.pop(0)
            else:
                s.pop(0)

        if operation != "":
            if operation == "*":
                accumulator *= int(digit)
            if operation == "/":
                accumulator //= int(digit)
        else:
            accumulator = int(digit)

        if is_negative:
            accumulator = - accumulator

        if len(s) > 0:
            if s[0] == "+":
                accumulator += self.calculate("".join(s[1:]))
            else:
                accumulator += self.calculate("".join(s[0:]))

        return accumulator


test_cases = [
    # "14/3*2",
    "0-2147483647"
]

solutions = [
    # 8,
    -2147483647
]

s = Solution()
for test, sol in zip(test_cases, solutions):
    actual = s.calculate(test)
    print(actual)
    print(sol)
    assert actual == sol
    print()






