"""
https://leetcode.com/problems/3sum/  (medium)

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
"""
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    return method2(nums)
    # return method1(nums)


def method1(nums: List[int]) -> List[List[int]]:
    """
    This method sort the list and then uses the two pointer approach on the rest of the array after fixing the one number
    :param nums:
    :return:
    """
    if len(nums) <= 2:
        return []

    nums = sorted(nums)

    solutions = dict()
    prev = None
    for index_fixed in range(0, len(nums) - 2):
        fixed_elem = nums[index_fixed]
        if prev is None or fixed_elem != prev:
            prev = fixed_elem
            lower_index = index_fixed + 1
            higher_index = len(nums) - 1

            while lower_index < higher_index:
                if fixed_elem + nums[lower_index] + nums[higher_index] == 0:
                    solutions["{}={}={}".format(*sorted([fixed_elem, nums[lower_index], nums[higher_index]]))] = [fixed_elem, nums[lower_index], nums[higher_index]]
                    lower_index += 1
                    higher_index -= 1
                else:
                    if fixed_elem + nums[lower_index] + nums[higher_index] < 0:
                        lower_index += 1
                    else:
                        higher_index -= 1

    return list(solutions.values())


def method2(nums: List[int]) -> List[List[int]]:
    """
    This approach uses the hashmap approach (similar to the 2sum) but on the subset array after removing one.
    It also uses a set to keep unique solutions
    :param nums:
    :return:
    """
    if len(nums) <= 2:
        return []

    solutions = dict()
    value_index_map = dict()
    for index, elem in enumerate(nums):
        index_list = value_index_map.get(elem, [])
        index_list.append(index)
        value_index_map[elem] = index_list

    for fix_elem_index, elem in enumerate(nums):
        current_map = value_index_map.copy()
        index_list = current_map[elem]
        if len(index_list) == 1:
            del current_map[elem]
        else:
            index_list.remove(fix_elem_index)
            current_map[elem] = index_list
        temp_sols = two_sum(current_map, -elem)
        for ts in temp_sols:
            ts.append(elem)
            solutions["{}={}={}".format(*sorted(ts))] = ts

    return list(solutions.values())


def two_sum(nums_map: dict, k) -> List[List[int]]:

    sol = []
    for num, index_list in nums_map.items():
        if k - num == num:
            if len(index_list) > 1:
                sol.append([num, k - num])
        else:
            if k - num in nums_map:
                sol.append([num, k - num])
    return sol



din = [
    [-1, 0, 1],
    [-1, 0, 1, 2, -1, -4],
    [-1, -1, 2],
    [],
    [0],
    [0, 0, 0, 0],
    [-2, 0, 0, 2, 2]
]

dout = [
    [[-1, 0, 1]],
    [[-1, -1, 2], [-1, 0, 1]],
    [[-1, -1, 2]],
    [],
    [],
    [[0, 0, 0]],
    [[-2, 0, 2]]
]

for data_in, expected_result in zip(din, dout):
    actual_result = three_sum(data_in)
    expected_result = [sorted(x) for x in expected_result]
    actual_result = [sorted(x) for x in actual_result]
    print(f"Expected: {expected_result}   Actual: {actual_result}")
    assert expected_result == actual_result
