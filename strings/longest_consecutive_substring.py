"""
Find the longest Consecutive Substring (Increasing Alphabetically) from the below pattern that starts with A.
You can assume ? as any character. it can be repace by 0 or 1 character.
Note: Consider all as upper case.

Example :
[?, B, A, ?, C, D, ?, ?, F, I, ?, ?, ?, ?, D, ?, ?, ?, H]
result 8
Exp: One of the Substrings is A, B, C, D, E, F from index 2 to 7.
But the longest substring can be formed from index 11 to 18 which A,B,C,D,E,F,G,H.
"""
from typing import List, Tuple

alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]


def check(ss: List[str], aphabet_pointer: int) -> int:
    if len(ss) == 0 or aphabet_pointer > len(alphabet):
        return 0

    max_sub_length = 0
    if ss[0] == alphabet[aphabet_pointer]:

        max_sub_length = check(ss[1:], aphabet_pointer + 1) + 1
    elif ss[0] == '?':
        max_sub_length = max(check(ss[1:], aphabet_pointer), check(ss[1:], aphabet_pointer + 1) + 1)

    return max_sub_length


def longest_consecutive_substring(s: List[str]) -> int:

    pointer = 0
    max_length = 0
    while pointer < len(s):
        c = s[pointer]
        if c == 'A' or c == '?':
            max_length_found = check(s[pointer:], 0)
            max_length = max(max_length, max_length_found)
        pointer += 1

    return max_length


din = [
    ['?', 'B', 'A', '?', 'C', 'D', '?', '?', 'F', 'I', '?', '?', '?', '?', 'D', '?', '?', '?', 'H'],
    ['?'] * 10,
    ['?', '?', '?', 'C', '?']
]

dout = [8, 10, 4]

for data_in, expected_result in zip(din, dout):
    actual = longest_consecutive_substring(data_in)
    print(actual)
    print(expected_result)
    assert actual == expected_result

# print(alphabet)