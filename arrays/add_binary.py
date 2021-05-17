"""
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/263/ (EASY)

Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""


def add_binary_sol_1(num1: str, num2: str):
    # sum - decimal value 18
    # binary value 10010
    sum = bin(int(num1, 2) + int(num2, 2))
    return sum


def one_digit_sum(a: str, b: str):
    if a == "1" and b == "1":
        return "1", "0"

    if a == "0" and b == "0":
        return "0", "0"

    return "0", "1"


def addBinary(a: str, b: str) -> str:
    if len(a) == 0:
        return b

    if len(b) == 0:
        return a

    m_len = max(len(a), len(b))
    pos = -1
    carry_over = "0"
    result = []

    while abs(pos) <= m_len:

        da = "0"
        if abs(pos) <= len(a):
            da = a[pos]

        db = "0"
        if abs(pos) <= len(b):
            db = b[pos]

        carry_over_temp_1, temp_val = one_digit_sum(da, db)
        carry_over_temp_2, val = one_digit_sum(carry_over, temp_val)

        _, carry_over = one_digit_sum(carry_over_temp_1, carry_over_temp_2)
        result.append(val)

        pos -= 1

    if carry_over == "1":
        result.append(carry_over)

    return "".join(result[::-1])


din = [
    ("11", "1"),
    ("1010", "1011")
]

dout = [
    "100",
    "10101"
]

for i, expected in zip(din, dout):
    actual = addBinary(i[0], i[1])
    print(actual)
    assert actual == expected
