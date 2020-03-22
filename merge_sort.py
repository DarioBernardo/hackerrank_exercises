# Merge sort
import numpy as np

print("Implementing merge sort! cool!")
my_pool = list(range(0, 100))
# print(my_pool)
my_array = np.random.choice(my_pool, len(my_pool), replace=False)

print(my_array)
print(f"Array length: {len(my_array)}")


def merge_sort(my_array):
    res = []
    if len(my_array) == 2:
        if my_array[0] > my_array[1]:
            res.append(my_array[1])
            res.append(my_array[0])
        else:
            res.append(my_array[0])
            res.append(my_array[1])

        return res.copy()

    if len(my_array) == 1:
        return my_array.copy()

    half_size = int(len(my_array) / 2)
    first_half = my_array[0:half_size]
    # print(len(first_half))
    second_half = my_array[half_size:len(my_array)]
    # print(len(second_half))

    res_first_half = merge_sort(first_half)
    res_second_half = merge_sort(second_half)

    index_1 = 0
    index_2 = 0

    # print(res_first_half)
    # print(res_second_half)

    while len(res) < (len(res_first_half) + len(res_second_half)):
        if index_2 >= len(res_second_half):
            res.append(res_first_half[index_1])
            index_1 = index_1 + 1
            continue

        if index_1 >= len(res_first_half):
            res.append(res_second_half[index_2])
            index_2 = index_2 + 1
            continue

        if res_first_half[index_1] > res_second_half[index_2]:
            res.append(res_second_half[index_2])
            index_2 = index_2 + 1
        else:
            res.append(res_first_half[index_1])
            index_1 = index_1 + 1

    # print(f"result {res}")

    return res.copy()


my_result = merge_sort(my_array)

print(f"Ordered array of {len(my_result)} elems: ")
print(my_result)

assert my_result == my_pool
print("ALL GOOD!")
