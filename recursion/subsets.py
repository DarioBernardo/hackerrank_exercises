"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:

    def gen_subsets(nums: List[int], current_sol: List[List[int]]) -> List[List[int]]:
        my_sol = [current_sol]
        for i in range(0, len(nums)):
            new_sol = current_sol.copy()
            new_sol.append(nums[i])
            my_sol.extend(gen_subsets(nums[i + 1:], new_sol))
        return my_sol

    sol = gen_subsets(nums, [])
    return list(sol)


din = [
    [1, 2, 3],
    [0]
]

expected_results = [
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
    [[], [0]]
]

for i, expected in zip(din, expected_results):
    actual = subsets(i)
    print(actual)
    print(expected)
    # assert actual == expected