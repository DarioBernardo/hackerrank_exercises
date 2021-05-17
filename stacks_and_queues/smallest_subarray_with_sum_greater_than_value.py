"""
Smallest subarray with sum greater than a given value
https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/  (easy-medium)

 Last Updated : 11 Feb, 2021
Given an array of integers and a number x, find the smallest subarray with sum greater than the given value.

Examples:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}

arr[] = {1, 2, 4}
    x = 8
Output : Not Possible
Whole array sum is smaller than 8.
"""

din = [
    ([1, 4, 45, 6, 0, 19], 51),
    ([1, 10, 5, 2, 7], 9),
    ([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280),
    ([1, 2, 4], 8)
]

dout = [
    3,
    1, 4,
    -1]


def smallest_sub_with_sum(nums, s) -> int:

    if len(nums) == 0:
        return -1

    if s <= 0:
        return 0

    start = 0
    end = 0

    sols = []

    running_total = 0
    while end < len(nums):
        running_total += nums[end]
        while running_total < s and end+1 < len(nums):
            end += 1
            running_total += nums[end]

        while running_total - nums[start] > s:
            running_total -= nums[start]
            start += 1

        if running_total > s:
            sols.append(end-start+1)

        end += 1

    if len(sols) == 0:
        return -1

    return min(sols)


for i, expected in zip(din, dout):
    actual = smallest_sub_with_sum(i[0], i[1])
    print(actual)
    assert actual == expected
