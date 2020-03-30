"""
Problem explained here:
https://www.geeksforgeeks.org/next-greater-element/ (solution provided at link is wrong)
"""

from collections import deque

test_cases = [
    [2, 6, 1, 12],
    [1, 2, 3, 5, 1, 13, 3],
    [3, 5, 4, 7, 6, 2],
    [80, 5, 4, 6, 8, 10, 5],
    [5, 3, 2, 1, 4]

]

solutions = [
    [6, 12, 12, -1],
    [2, 3, 5, 13, 13, -1, -1],
    [5, 7, 7, -1, -1, -1],
    [-1, 6, 6, 8, 10, -1, -1],
    [-1, 4, 4, 4, -1]
]


def riddle(arr):
    riddle_sol = []
    stack = deque()

    for i, elem in enumerate(arr):
        popped = []
        while len(stack) > 0 and stack[-1] < elem:
            popped.append(stack.pop())
            del riddle_sol[-1]

        for _ in popped:
            riddle_sol.append(elem)

        stack.append(elem)
        riddle_sol.append(-1)

    return riddle_sol


for test, sol in zip(test_cases, solutions):
    span = riddle(test)
    print(span)
    print(sol)
    assert span == sol
    print()

print("Done!")

