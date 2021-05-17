"""
Find First and Last Position of Element in Sorted Array

Solution
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""
from typing import List

"""
[1, 3, 3, 5, 5, 5, 8, 9, 10] 9
target = 3

lo = 
hi = 1
pointer = 0


"""

def search_bound(nums: list, target: int, left: bool = True):
    lo = 0
    hi = len(nums)

    while lo < hi:
        pointer = (lo + hi) // 2
        if nums[pointer] > target or (left and target == nums[pointer]):
            hi = pointer
        else:
            lo = pointer + 1

    return lo


def searchRange(nums: List[int], target: int) -> List[int]:

    if len(nums) == 0:
        return [-1, -1]

    if len(nums) == 1:
        if nums[0] == target:
            return [0, 0]
        else:
            return [-1, -1]

    left_pointer = search_bound(nums, target, True)
    if left_pointer == len(nums) or nums[left_pointer] != target:
        return [-1, -1]

    right_pointer = search_bound(nums, target, False)
    return [left_pointer, right_pointer-1]


din = [
    ([1, 2, 4, 5, 6, 7, 9, 11, 13, 14], 2),
    ([1, 3, 3, 5, 5, 5, 8, 9, 10], 4),
    ([1, 3, 3, 5, 5, 5, 8, 9, 10, 11], 5),
    ([1, 3, 3, 5, 5, 5, 8, 9, 10], 9),
    ([1, 3], 1)
]

expected_out = [
    [1, 1],
    [-1, -1],
    [3, 5],
    [7, 7],
    [0, 0]
]

for i, expected in zip(din, expected_out):
    actual = searchRange(i[0], i[1])
    print(actual)
    assert actual == expected
