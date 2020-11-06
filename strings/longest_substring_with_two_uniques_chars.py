"""
      Longest substring with at most two unique characters
Exercise taken from:
https://algorithms.tutorialhorizon.com/longest-substring-with-at-most-two-unique-characters/

Objective: Given a string, write an algorithm to find the longest substring with at most two characters.

Example:

Input: aabbccddc
Output: ccddc, length: 5

Input: aabacbeeeebeaabb
Output: beeeebe, length 7

Input: aaaaaa
Output: Only one unique character is present in the input string

"""

data = [
    ("aabbccddc", "ccddc"),
    ("ggabababaaabababfffff", "abababaaababab"),
    ("aabacbeeeebeaabb", "beeeebe"),
    ("aaaaaa", "aaaaaa"),
    ("cxxdaaaaaarg", "daaaaaa"),
    ("c", "c")
]


def check_summary(char, summary):
    counter = 0
    for key, value in summary.items():
        if char != key and value > 0:
            counter += 1

    if counter > 1:
        return False
    return True


def add_to_summary(c, summary):
    char_counter = summary.get(c, 0)
    summary[c] = char_counter + 1


def remove_from_summary(c, summary):
    char_counter = summary.get(c, 1)
    summary[c] = char_counter - 1


def riddle(s: str):

    if len(s) <= 2:
        return s

    start = 0
    end = 0
    sol = []
    summary = {}

    while end < len(s):
        c = s[end]
        if check_summary(c, summary):
            add_to_summary(c, summary)
            if end+1 - start > len(sol):
                sol = s[start:end+1]

            end += 1
        else:
            while not check_summary(c, summary):
                char_to_remove = s[start]
                remove_from_summary(char_to_remove, summary)
                start += 1

    if end-start > len(sol):
        sol = s[start:end]

    return sol


for data_in, expected_result in data:
    actual_result = riddle(data_in)
    print(f"Actual:   {actual_result}")
    print(f"Expected: {expected_result}\n")
    assert actual_result == expected_result

print("DONE!")
