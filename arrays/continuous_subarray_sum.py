"""
https://leetcode.com/problems/continuous-subarray-sum/   MEDIUM

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two
whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.



Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
"""
from typing import List


def checkSubarraySum(nums: List[int], k: int) -> bool:
    if len(nums) == 0:
        return False

    cum_sum = 0
    reminders_map = {0: 0}
    for i, n in enumerate(nums, 1):
        cum_sum += n
        reminder = cum_sum % k
        if reminder in reminders_map:
            if reminders_map[reminder] <= i - 2:
                return True
        else:
            reminders_map[reminder] = i

    return False


test_cases = [
    ([0], 1),
    ([5, 0, 0, 0, 0], 3),
    ([23, 2, 4, 6, 7], 6),
    ([23, 2, 6, 4, 7], 13)
]

solutions = [
    False,
    True,
    True,
    False
]

for test, sol in zip(test_cases, solutions):
    span = checkSubarraySum(test[0], test[1])
    print(span)
    print(sol)
    assert span == sol
    print()

print("Done!")
