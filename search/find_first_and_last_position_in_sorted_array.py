"""
https://www.programcreek.com/2014/04/leetcode-search-for-a-range-java/

Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n). If the target is not found in the array, return [-1, -1].
For example, given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].

Analysis: Based on the requirement of O(log n), this is a binary search problem apparently.
"""
from typing import List, Tuple


def search_range(arr: List[int], target: int) -> Tuple[int, int]:

    if len(arr) == 0:
        return -1, -1

    def find_lower_bound(a: List[int], t: int) -> int:
        low = 0
        high = len(a)-1
        while low < high:
            mid = (low + high) // 2
            if a[mid] < t:
                low = mid + 1
            else:
                high = mid

        if low < len(a) and a[low] == t:
            return low

        return -1

    def find_upper_bound(a: List[int], t: int) -> int:
        low = 0
        high = len(a) - 1
        while low < high:
            mid = (low + high) // 2 + 1
            if a[mid] > t:
                high = mid - 1
            else:
                low = mid

        if high < len(a) and a[high] == t:
            return low

        return -1

    lower_bound = find_lower_bound(arr, target)
    if lower_bound == -1:
        return -1, -1
    upper_bound = find_upper_bound(arr, target)

    return lower_bound, upper_bound


din = [
    ([5, 7, 7, 8, 8, 10], 8),
    ([2, 2, 2, 5, 5, 7, 7, 8, 8, 9, 9, 9, 10, 10], 2),
    ([2, 2, 2, 5, 5, 7, 7, 8, 8, 9, 9, 9, 10, 10], 3),
    ([2, 2, 2, 5, 5, 7, 7, 8, 8, 9, 9, 9, 10, 10], 7),
    ([2, 2, 2, 5, 5, 7, 7, 8, 8, 9, 9, 9, 10, 10], 10),
    ([2, 2, 2, 5, 5, 7, 7, 8, 8, 9, 9, 9, 10, 10], 11)
]

dout = [
    (3, 4),
    (0, 2),
    (-1, -1),
    (5, 6),
    (12, 13),
    (-1, -1)
]


for data_in, expected in zip(din, dout):
    actual = search_range(data_in[0], data_in[1])
    print(f"Result is: {actual} expected {expected}")
    assert actual == expected
