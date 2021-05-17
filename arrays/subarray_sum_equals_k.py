"""
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3019/
Medium/hard

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""
"""
SOLUTION:
Algorithm

The idea behind this approach is as follows: If the cumulative sum(represented by sum[i]sum[i] for sum up to i^{th}i 
th index) up to two indices is the same, the sum of the elements lying in between those indices is zero. 
Extending the same thought further, if the cumulative sum up to two indices, say ii and jj is at a difference of kk i.e. 
if sum[i] - sum[j] = ksum[i]−sum[j]=k, the sum of elements lying between indices ii and jj is kk.

Based on these thoughts, we make use of a hashmap mapmap which is used to store the cumulative sum up to all the indices 
possible along with the number of times the same sum occurs. 
We store the data in the form: (sum_i, no. of occurrences of sum_i)(sum i,no.ofoccurrencesofsum i). 
We traverse over the array numsnums and keep on finding the cumulative sum. 
Every time we encounter a new sum, we make a new entry in the hashmap corresponding to that sum. 
If the same sum occurs again, we increment the count corresponding to that sum in the hashmap. 
Further, for every sum encountered, we also determine the number of times the sum sum-ksum−k has occurred already, 
since it will determine the number of times a subarray with sum kk has occurred up to the current index.
 We increment the countcount by the same amount.

After the complete array has been traversed, the countcount gives the required result.
"""


from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        if nums[0] == k:
            return 1
        else:
            return 0

    cum_sum = 0
    sums_dict = {cum_sum: 1}
    counter = 0

    for n in nums:
        cum_sum += n
        if cum_sum - k in sums_dict:
            counter += sums_dict[cum_sum - k]

        this_sum_freq = sums_dict.get(cum_sum, 0)
        this_sum_freq += 1
        sums_dict[cum_sum] = this_sum_freq

    return counter

def subarray_sum(nums: List[int], k: int) -> int:
    if len(nums) == 0:
        return 0

    cum_sum = 0
    for n in nums:
        cum_sum += n

din = [
    ([1, 1, 1], 2),
    ([1, 2, 3], 3),
    ([1, -1, 0], 0),
    ([-1, -1, 1], 0)
]

expected_results = [
    2,
    2,
    3,
    1
]

for i, expected in zip(din, expected_results):
    actual = subarray_sum(i[0], i[1])
    print(actual)
    print(expected)
    assert actual == expected
