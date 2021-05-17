"""
Insert a new elem in a sorted list in O(log N)
"""
import random
from typing import List


def insert_elem(in_list: List, val: int):
    if len(in_list) == 0:
        in_list.append(elem)
        return

    start = 0
    end = len(in_list)
    while start < end:
        middle = start + int((end - start) / 2)
        if in_list[middle] > val:
            end = middle
        else:
            start = middle + 1

    in_list.insert(start, val)


INPUT_LIST_SIZE = 20
NUMBER_OF_TESTS = 10

for _ in range(0, NUMBER_OF_TESTS):
    input_list = sorted(list([random.randint(-int(INPUT_LIST_SIZE/2), int(INPUT_LIST_SIZE/2)) for _ in range(0, INPUT_LIST_SIZE)]))

    elem = random.randint(-int(INPUT_LIST_SIZE/2), int(INPUT_LIST_SIZE/2))
    solution = input_list.copy()
    solution.append(elem)
    solution = sorted(solution)
    insert_elem(input_list, elem)

    print(input_list)
    print(solution)
    assert solution == input_list


input_list = [0, 0, 0, 0, 0]
insert_elem(input_list, 1)

print(input_list)
print([0, 0, 0, 0, 0, 1])
assert [0, 0, 0, 0, 0, 1] == input_list




