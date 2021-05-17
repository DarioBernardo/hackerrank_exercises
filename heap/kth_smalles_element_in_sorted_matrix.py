"""

"""
from typing import List, Tuple


def heapify_up(h: List[Tuple[int, int, int]]):
    child = len(h) - 1
    parent = (child - 1) // 2
    while h[child][0] < h[parent][0] and parent >= 0:
        h[parent], h[child] = h[child], h[parent]
        child = parent
        parent = (child - 1) // 2


def heapify_down(h: List[Tuple[int, int, int]]):
    current = 0
    left_child_index = 1
    right_child_index = 2
    while len(h) > left_child_index:
        child_to_swap = left_child_index
        if len(h) > right_child_index and h[left_child_index] > h[right_child_index]:
            child_to_swap = right_child_index

        if h[current] < h[child_to_swap]:
            break
        else:
            h[current], h[child_to_swap] = h[child_to_swap], h[current]

        current = child_to_swap
        left_child_index = 2 * current + 1
        right_child_index = 2 * current + 2


def heappush(h: List[Tuple[int, int, int]], val: Tuple[int, int, int]):
    if len(h) == 0:
        h.append(val)
        return

    h.append(val)
    heapify_up(h)


def heappop(h: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
    elem = h.pop(0)
    if len(h) > 0:
        end = h.pop()
        h.insert(0, end)
        heapify_down(h)
    return elem


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        if len(matrix) == 0 or k > len(matrix) * len(matrix[0]):
            return None

        #### METHOD 1
        #         pointers = [0] * len(matrix)

        #         chosen_elem = None
        #         for i in range(0, k):
        #             min_pointer = 0
        #             current_min = None
        #             for pointer_number, pointer_position in enumerate(pointers):
        #                 if pointer_position < len(matrix):
        #                     if current_min is None or current_min > matrix[pointer_number][pointer_position]:
        #                         current_min = matrix[pointer_number][pointer_position]
        #                         min_pointer = pointer_number

        #             chosen_elem = current_min
        #             pointers[min_pointer] += 1

        #         return chosen_elem

        ### METHOD 2 - Heap of pointers

        heap = []
        for pointer in range(0, len(matrix)):
            heap_val = matrix[pointer][0], pointer, 0
            heappush(heap, heap_val)

        sol = []
        for i in range(0, k):
            elem = heappop(heap)
            sol.append(elem[0])
            pointer = elem[1]
            position = elem[2] + 1
            if position < len(matrix[0]):
                heappush(heap, (matrix[pointer][position], pointer, position))

        return sol[-1]


test_cases = [
    ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
]

solutions = [
    13,
    5
]

for test, sol in zip(test_cases, solutions):
    s = Solution()
    span = s.kthSmallest(test[0], test[1])
    print(span)
    print(sol)
    assert span == sol
    print()








