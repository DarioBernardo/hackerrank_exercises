"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
"""


def longest_valid_parentheses(s: str) -> int:
    if len(s) <= 1:
        return 0

    """
    )()())
    )()(())(

    stack = []
    current_strike_start_index = None
    max_length = 2

    index = 6
    p = )
    """

    stack = []
    max_length = 0
    current_strike_start_index = None
    for index, p in enumerate(s):
        if p == "(":
            if current_strike_start_index is not None:
                stack.append(current_strike_start_index)
                current_strike_start_index = None
            else:
                stack.append(index)
        else:
            if len(stack) > 0:
                open_index = stack.pop()
                current_strike_start_index = open_index
                max_length = max(max_length, index - open_index + 1)
            else:
                current_strike_start_index = None

    return max_length


din = [
    "(()",
    ")()())",
    "",
    ")()(((()()))))(",
    ")()(()()))()()(()())"
]

dout = [
    2,
    4,
    0,
    12,
    10
]


for data_in, expected_result in zip(din, dout):
    actual_result = longest_valid_parentheses(data_in)
    print(f"Expected: {expected_result}   Actual: {actual_result}")
    assert expected_result == actual_result
