"""
ACTUAL INTERVIEW QUESTION (22 March 2021)

given an array of integers `arr` return true if there are duplicates within a certain distance k.

Example 1:
arr = [1, 2, 4, 1, 3]
k = 4
Output: True
Explanation: elements in position 0 and 3 ar both `1`s. Their distance is 4, hence True.

Example 2:
arr = [1, 2, 4, 1, 3]
k = 3
Output: False
Explanation: elements in position 0 and 3 ar both `1`s. Their distance is 4, hence False.

Example 3:
arr = [1, 2, 4, 1, 3, 1, 5]
k = 3
Output: True
Explanation: elements in position 0 and 3 ar both `1`s. But their distance is 4, but the distance between elem in position 3 and 5 is 2 hence True.


Note:
    Can you optimise space?
"""
from typing import List


def find_duplicates(arr: List, k: int) -> bool:
    if len(arr) == 0 or k <= 0:
        return False

    last_seen_map = dict()

    for pos, n in enumerate(arr):
        last_seen = last_seen_map.get(n, None)
        if last_seen is not None:
            if pos - last_seen < k:
                return True

        last_seen_map[n] = pos

    return False


din = [
    ([1, 2, 4, 1, 3], 3),
    ([1, 2, 4, 1, 3, 1, 5], 3)
]

dout = [False, True]


for data_in, expected in zip(din, dout):
    actual = find_duplicates(data_in[0], data_in[1])
    print(f"Result is: {actual} expected {expected}")
    assert actual == expected
