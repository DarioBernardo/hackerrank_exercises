# Quick sort
import numpy as np
import random

print("Implementing quick sort! cool!")
my_pool = list(range(0, 50))
print(my_pool)
my_array = np.random.choice(my_pool, len(my_pool), replace=False)

print(my_array)
print(f"Array length: {len(my_array)}")


def quick_sort(data: list) -> list:

    def _swap(data, src, dest):
        temp = data[src]
        data[src] = data[dest]
        data[dest] = temp

    if len(data) <= 1:
        return data

    if len(data) == 2:
        if data[0] < data[1]:
            return data
        else:
            _swap(data, 0, 1)

    pivot_index = random.randint(0, len(data)-1)
    # print(pivot_index)
    left_index = 0
    right_index = len(data)-1

    compare_value = data[pivot_index]
    while right_index > left_index:

        while right_index > left_index and data[left_index] < compare_value:
            left_index += 1

        while right_index > left_index and data[right_index] > compare_value:
            right_index -= 1

        if right_index > left_index:
            _swap(data, left_index, right_index)

    left_half = data[0:left_index]
    right_half = data[left_index:len(data)]

    left_sort = quick_sort(left_half)
    right_sort = quick_sort(right_half)

    return list(np.append(left_sort, right_sort, axis=0))


my_result = quick_sort(my_array)

print(f"Ordered array of {len(my_result)} elems: ")
print(my_result)

assert my_result == my_pool
print("ALL GOOD!")