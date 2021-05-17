"""
https://leetcode.com/problems/3sum-closest/
https://www.programcreek.com/2013/02/leetcode-3sum-closest-java/

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.


Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
        """
        [-4,-1,2,1] 1

        closest_sum = 2
        sol = [-4 2 1]

        pos = 1
        n = -1

        i = 2
        j = 3
        k = 5


        """

        closest_sum = None
        sol = None

        nums = sorted(nums)

        for pos, n in enumerate(nums):
            i = pos + 1
            j = len(nums) - 1
            k = target - n
            while i < j:
                if nums[i] + nums[j] == k:
                    return nums[i] + nums[j] + n
                if closest_sum is None or closest_sum > abs(target - n - nums[i] - nums[j]):
                    closest_sum = abs(target - n - nums[i] - nums[j])
                    sol = n + nums[i] + nums[j]

                if nums[i] + nums[j] < k:
                    i += 1
                else:
                    j -= 1

        return sol


din = [
    ([-4, -1, 2, 1], 1),
    ([0, -4, 1, -5], 0)
]

dout = [
    2,
    -3
]


for data_in, expected in zip(din, dout):
    actual = three_sum_closest(data_in[0], data_in[1])
    print(f"Result is: {actual} expected {expected}")
    assert actual == expected





