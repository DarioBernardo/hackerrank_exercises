"""
MEDIUM (for me EASY)
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
 You may return the answer in any order.
 Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    if len(nums) == 0 or k == 0:
        return []

    counter_map = dict()

    for n in nums:
        counter = counter_map.get(n, 0)
        counter_map[n] = counter + 1

    items = sorted(list(counter_map.items()), key=lambda tup: tup[1], reverse=True)
    solution = []
    for n, counter in items[0:k]:
        solution.append(n)

    return solution


test_cases = [
    ([1, 1, 1, 2, 2, 3], 2),
    ([3, 0, 1, 0], 1)
]

solutions = [
    [1, 2],
    [0]
]

for test, sol in zip(test_cases, solutions):
    span = top_k_frequent(test[0], test[1])
    print(span)
    print(sol)
    assert sorted(span) == sorted(sol)
    print()

print("Done!")