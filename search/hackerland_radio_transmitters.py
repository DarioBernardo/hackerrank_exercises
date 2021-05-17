"""
MEDIUM/HARD
https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
"""


# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    if len(x) == 1:
        return 1

    arr = sorted(x)

    antennass_needed = 0
    last_antenna_position = None
    for pos in range(0, len(arr)):
        house = arr[pos]
        if not last_antenna_position or last_antenna_position + k < house:
            possible_antenna_position = pos
            while possible_antenna_position + 1 < len(arr) and arr[possible_antenna_position + 1] - house <= k:
                possible_antenna_position += 1

            last_antenna_position = arr[possible_antenna_position]
            antennass_needed += 1

    return antennass_needed


input_list = [
    ([1, 2, 3, 4, 5], 1),
    ([7, 2, 4, 6, 5, 9, 12, 11], 2)
]

expected_list = [2, 3]

for i, expected in zip(input_list, expected_list):
    actual = hackerlandRadioTransmitters(i[0], i[1])
    assert actual == expected
