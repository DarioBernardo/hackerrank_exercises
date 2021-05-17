from typing import List


def swap(nums, a, b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp


def move_zeroes(nums: List[int]) -> None:
    if len(nums) == 1:
        return

    # Two pointer approach, one pointer to the first zero found, the last to the first
    # non zero element after the first zero found.

    for zero_pointer in range(0, len(nums) - 1):
        if nums[zero_pointer] == 0:
            non_zero_pointer = zero_pointer + 1
            while nums[non_zero_pointer] == 0:
                non_zero_pointer += 1
                if non_zero_pointer == len(nums):
                    return

            swap(nums, zero_pointer, non_zero_pointer)


din = [0, 1, 0, 3, 12]

move_zeroes(din)

print(din)
assert din == [1, 3, 12, 0, 0]
