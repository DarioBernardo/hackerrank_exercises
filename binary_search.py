import numpy as np


ARRAY_LENGTH = 50

print("Implementing binary search algorithm! cool!")
my_pool = list(range(0, ARRAY_LENGTH * 2))
# print(my_pool)
my_array = sorted(np.random.choice(my_pool, ARRAY_LENGTH, replace=False))
print(my_array)


def find_index_of(arr: list, value: int) -> int:
    if arr is None:
        return -1

    if len(arr) == 0:
        return -1

    if len(arr) == 1:
        return 0

    if len(arr) == 2:
        if arr[0] == value:
            return 0
        if arr[1] == value:
            return 1
        return -1

    mid_point = int(len(arr)/2)
    if arr[mid_point] > value:
        return find_index_of(arr[0:mid_point], value)
    else:
        return mid_point + find_index_of(arr[mid_point:len(arr)], value)


for elem in my_array:
    index = find_index_of(my_array, elem)
    assert elem == my_array[index]

print("ALL GOOD!")
