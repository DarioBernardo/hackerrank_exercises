from typing import List


def merge(nums1: List[int], nums2: List[int]) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    n2_pointer = len(nums2)-1
    n1_pointer = len(nums1)-1-len(nums2)

    current_pos = len(nums1)-1
    while current_pos >= 0:
        num1_val = nums1[n1_pointer]
        if n1_pointer < 0 or n2_pointer >= 0 and num1_val < nums2[n2_pointer]:
            nums1[current_pos] = nums2[n2_pointer]
            n2_pointer -= 1
        else:
            nums1[current_pos] = num1_val
            n1_pointer -= 1

        current_pos -= 1


n1 = [1, 2, 3, 0, 0, 0]
n2 = [2, 5, 6]
merge(n1, n2)
print(n1)

