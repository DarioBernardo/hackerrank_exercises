from typing import List


def find_pivot(nums: List[int]) -> int:
    lo = 0
    hi = len(nums)-1

    while lo < hi:
        mid = (lo + hi) // 2

        if mid + 1 >= len(nums):
            return -1

        if nums[mid] > nums[mid + 1]:
            return mid
        if nums[mid] < nums[lo]:
            hi = mid
        else:
            lo = mid + 1


    return -1


def binary_search(nums: List[int], target: int) -> int:
    lo = 0
    hi = len(nums)

    """
    [0,1,2,4,5,6,7]
    """

    while lo < hi:
        mid = (lo + hi) // 2
        if target == nums[mid]:
            return mid
        elif nums[mid] > target:
            hi = mid
        else:
            lo = mid + 1

    return -1


def search(nums: List[int], target: int) -> int:
    # find rotation index first

    pivot_point = find_pivot(nums)

    if pivot_point == -1:
        return binary_search(nums, target)

    if nums[pivot_point] == target:
        return pivot_point

    result = -1
    if nums[0] <= target < nums[pivot_point]:
        result = binary_search(nums[:pivot_point], target)
    elif nums[pivot_point+1] <= target <= nums[len(nums) - 1]:
        index = binary_search(nums[pivot_point+1:], target)
        if index == -1:
            return -1
        else:
            result = pivot_point+1+index

    return result


din = [
    ([4,5,6,7,0,1,2], 0),
    ([1,3,5], 5),
    ([5,1,3], 2),
    ([2,3,4,5,1], 1),
    # ([1, 3], 1)
]

expected_out = [
    4,
    2,
    -1,
    4,
    # [0, 0]
]

for i, expected in zip(din, expected_out):
    actual = search(i[0], i[1])
    print(actual)
    assert actual == expected
