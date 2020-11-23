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


def riddle(s: str):
    change_char_index = -1
    start_index = 0
    best_start_index = 0
    best_end_index = 0
    current = 0
    char_set = set()

    while current < len(s):
        c = s[current]
        char_set.add(c)

        if len(char_set) <= 2:
            if len(char_set) == 2 and change_char_index < 0:
                change_char_index = current

            current += 1

            if current - start_index > best_end_index - best_start_index:
                best_end_index = current
                best_start_index = start_index

        elif len(char_set) == 3:
            char_set = set()
            current = change_char_index
            start_index = change_char_index
            change_char_index = -1

    return s[best_start_index:best_end_index]


for data_in, expected_result in data:
    actual_result = riddle(data_in)
    print(f"Actual:   {actual_result}")
    print(f"Expected: {expected_result}\n")
    assert actual_result == expected_result

print("DONE!")
