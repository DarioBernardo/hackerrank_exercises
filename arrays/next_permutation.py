"""
https://leetcode.com/problems/next-permutation/ (MEDIUM)
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(n, start):
            for i in range(start, (start + len(n)) // 2):
                n[i], n[len(n) - 1 - i + start] = n[len(n) - 1 - i + start], n[i]

        for i in range(len(nums) - 1, 0, -1):
            next_number = i - 1
            if nums[i] > nums[next_number]:
                num_to_swap = i
                while num_to_swap + 1 < len(nums) and nums[next_number] < nums[num_to_swap + 1]:
                    num_to_swap += 1

                nums[next_number], nums[num_to_swap] = nums[num_to_swap], nums[next_number]
                reverse(nums, next_number+1)
                return

        reverse(nums, 0)


test_cases = [
    # [1,2,3],
    # [3,2,1],
    # [1, 3, 2],
    [1,3,2],
    # [4, 2, 0, 2, 3, 2, 0]
]

solutions = [
    # [1,3,2],
    # [1,2,3],
    # [2, 1, 3],
    [2,1,3]
    # [4, 2, 0, 3, 0, 2, 2]
]

s = Solution()
for test, sol in zip(test_cases, solutions):
    s.nextPermutation(test)
    print(test)
    print(sol)
    assert test == sol
    print()
