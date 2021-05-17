from typing import List


def find_kth_positive(arr: List[int], k: int) -> int:

    if len(arr) == 0:
        return k - 1

    def is_number_in_array(a: List[int], val: int) -> bool:

        start = 0
        end = len(a)
        while start < end:
            middle = start + (end - start) // 2
            if a[middle] == val:
                return True
            elif a[middle] < val:
                start = middle + 1
            else:
                end = middle

        return False

    counter = 0
    current_val = 1
    while counter < k:
        if not is_number_in_array(arr, current_val):
            counter += 1

        current_val += 1

    return current_val-1


din = [
    ([1, 2], 1),
    ([2, 3, 4, 7, 11], 5)
]

dout = [
    3,
    9,
]


for data_in, expected_result in zip(din, dout):
    actual_result = find_kth_positive(data_in[0], data_in[1])
    print(f"Expected: {expected_result}   Actual: {actual_result}")
    assert expected_result == actual_result







