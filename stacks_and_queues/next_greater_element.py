"""
Problem explained here:
https://www.geeksforgeeks.org/next-greater-element/ (solution provided at link is wrong)
"""


test_cases = [
    [2, 6, 1, 12],
    [11, 11, 10, 5, 4, 10, 11],
    [1, 2, 3, 5, 1, 13, 3],
    [3, 5, 4, 7, 6, 2],
    [80, 5, 4, 6, 8, 10, 5],
    [5, 3, 2, 1, 4]

]

solutions = [
    [6, 12, 12, -1],
    [-1, -1, 11, 10, 10, 11, -1],
    [2, 3, 5, 13, 13, -1, -1],
    [5, 7, 7, -1, -1, -1],
    [-1, 6, 6, 8, 10, -1, -1],
    [-1, 4, 4, 4, -1]
]


def riddle(arr):
    # DO INPUT CHECKS
    if len(arr) == 1:
        return [-1]

    for e in arr:
        if not isinstance(e, int) or e < 0 or e > 100_000_000_000:
            raise Exception("BLA BLA")
    ###

    riddle_sol = [-1] * len(arr)
    stack = []
    indexes = []

    for pos, elem in enumerate(arr):

        while len(stack) > 0 and elem > stack[-1]:
            del stack[-1]
            delete_elem_pos = indexes.pop(-1)
            riddle_sol[delete_elem_pos] = elem

        stack.append(elem)
        indexes.append(pos)

    return riddle_sol


for test, sol in zip(test_cases, solutions):
    span = riddle(test)
    print(span)
    print(sol)
    assert span == sol
    print()

print("Done!")

