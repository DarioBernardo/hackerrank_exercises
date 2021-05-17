"""
Question briefly mentioned in Day 2b
https://leetcode.com/discuss/interview-question/1158980/Facebook-or-E5-or-MLE-or-Menlo-Park

couldn't find actual question

Find the length of the longest sub-array whose sum is target
"""
from typing import List


def longest_subarray_sum_k(arr: List[int], k: int) -> int:

    if len(arr) == 0:
        return 0

    cum_sum = 0
    cum_sum_map = {0: 0}
    max_length = 0
    for i, n in enumerate(arr, 1):
        cum_sum += n
        difference = cum_sum - k
        if difference in cum_sum_map:
            if max_length < i - cum_sum_map[difference]:
                max_length = i - cum_sum_map[difference]

        if cum_sum not in cum_sum_map:
            cum_sum_map[cum_sum] = i

    return max_length


test_cases = [
    ([23, 2, 4, 6, 7], 6),
    ([23, 2, 6, 4, 13], 25),
    ([23, 2, 4, 1, -1, 6, 7], 6),
]

solutions = [
    2,
    4,
    4
]

for test, sol in zip(test_cases, solutions):
    span = longest_subarray_sum_k(test[0], test[1])
    print(span)
    print(sol)
    assert span == sol
    print()

print("Done!")
