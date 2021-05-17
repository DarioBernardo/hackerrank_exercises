"""
https://leetcode.com/problems/target-sum/ (MEDIUM)

You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.


Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3


Example 2:

Input: nums = [1], target = 1
Output: 1
"""
from typing import List

cache = dict()


def translate_to_key(n: List[int]) -> str:
    s = ""
    for e in n:
        s += str(e) + "-"

    return s


# @cache
def possible_sums(nums: List[int]) -> List[int]:
    key = translate_to_key(nums)
    if key in cache:
        print("cache hit!")
        return cache[key]

    if len(nums) == 0:
        return [0]

    if len(nums) == 1:
        return [nums[0], -nums[0]]

    sol = []
    other_sums = possible_sums(nums[1:])
    for s in other_sums:
        sol.append(s + nums[0])
        sol.append(s - nums[0])

    cache[key] = sol
    return sol


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return 0

        solution = 0
        totals = possible_sums(nums)
        for t in totals:
            if t == target:
                solution += 1

        return solution


din = [
    ([1, 1, 1, 1, 1], 3),
    ([8, 48, 11, 47, 26, 12, 16, 39, 38, 50, 21, 12, 34, 1, 28, 1, 3, 9, 17, 50], 3)
]

expected_out = [
    5,
    6317,
]

s = Solution()
for i, expected in zip(din, expected_out):
    actual = s.findTargetSumWays(i[0], i[1])
    print(actual)
    assert actual == expected
