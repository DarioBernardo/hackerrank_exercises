"""
https://leetcode.com/problems/missing-element-in-sorted-array/  (MEDIUM for me HARD)
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k,
return the kth missing number starting from the leftmost number of the array.

NOTE: Solve it in O(log n)


Example 1:

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.


Example 2:

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.


Example 3:

Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

"""
from typing import List


def missing_element(nums: List[int], k: int) -> int:
    def missing(arr: List[int], j: int):
        return arr[j] - arr[0] - j

    if missing(nums, len(nums) - 1) < k:
        still_missing = k - missing(nums, len(nums) - 1)
        return still_missing + nums[len(nums) - 1]

    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if missing(nums, mid) >= k:
            high = mid
        else:
            low = mid + 1

    return nums[low] + k - missing(nums, low) - 1


test_cases = [
    ([4, 7, 9, 10], 1),
    ([4, 7, 9, 10], 3),
    ([1, 2, 4], 3),
]

solutions = [
    5,
    8,
    6
]

for test, sol in zip(test_cases, solutions):
    span = missing_element(test[0], test[1])
    print(span)
    print(sol)
    assert span == sol
    print()

print("Done!")