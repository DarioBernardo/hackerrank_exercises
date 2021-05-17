"""
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/3026/  (HARD)

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""
import math
from typing import List, Union


def is_free_land(x, y, g):
    return g[x][y] == 0


def is_obstacle(x, y, g):
    return g[x][y] == 2


def is_house(x, y, g):
    return g[x][y] == 1


def get_children(x, y, max_len_x, max_len_y) -> List[List[int]]:
    children = []
    if x > 0:
        children.append([x - 1, y])

    if x < max_len_x - 1:
        children.append([x + 1, y])

    if y > 0:
        children.append([x, y - 1])

    if y < max_len_y - 1:
        children.append([x, y + 1])

    return children


def hash_tuple(t: Union[tuple, list]) -> str:
    return "{}-{}".format(t[0], t[1])


def shortest_distance(grid: List[List[int]]) -> int:
    if len(grid) == 0:
        return -1

    x_size = len(grid)
    y_size = len(grid[0])

    min_cost = math.inf

    tot_number_of_houses = 0
    for x in range(0, x_size):
        for y in range(0, y_size):
            if is_house(x, y, grid):
                tot_number_of_houses += 1

    for x in range(0, x_size):
        for y in range(0, y_size):
            visited = set()
            costs = []

            if is_free_land(x, y, grid):
                visited.add(hash_tuple([x, y]))
                queue = [(x, y, 0)]
                while len(queue) != 0:

                    position_x, position_y, cost = queue.pop(0)
                    children = get_children(position_x, position_y, x_size, y_size)
                    for child in children:
                        if not is_obstacle(child[0], child[1], grid) and hash_tuple(child) not in visited:
                            visited.add(hash_tuple(child))
                            if is_house(child[0], child[1], grid):
                                costs.append(cost+1)
                            else:
                                queue.append((child[0], child[1], cost+1))

                    if len(costs) == tot_number_of_houses:
                        break

                if len(costs) == tot_number_of_houses:
                    min_cost = min(sum(costs), min_cost)
    if min_cost < math.inf:
        return min_cost

    return -1


"""
CASE 1:
Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
"""
"""
CASE 2:
Input: [[1,0,2,0,1],[0,2,2,0,0],[0,2,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 2 - 2 - 0 - 0
|   |   |   |   |
0 - 2 - 1 - 0 - 0
"""
"""
CASE 3:
Input: [[0,0,2,0,1],[0,2,2,0,0],[0,2,1,0,1]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 2 - 2 - 0 - 0
|   |   |   |   |
0 - 2 - 1 - 0 - 1
"""

din = [
    [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]],
    [[1, 0, 2, 0, 1], [0, 2, 2, 0, 0], [0, 2, 1, 0, 0]],
    [[0, 0, 2, 0, 1], [0, 2, 2, 0, 0], [0, 2, 1, 0, 1]],
    [[0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0],
     [0, 0, 2, 0, 0, 2, 0, 2, 0, 1, 0, 0, 0, 2, 0, 0, 2, 2, 2, 1, 0, 0, 2, 2, 0, 0, 0, 1, 2, 2, 2],
     [2, 0, 0, 0, 2, 1, 2, 0, 2, 0, 1, 2, 0, 0, 0, 2, 2, 2, 1, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 1, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0],
     [0, 2, 0, 1, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0],
     [2, 2, 2, 2, 2, 2, 0, 0, 1, 0, 0, 0, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 1],
     [2, 2, 0, 0, 2, 2, 2, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0],
     [0, 0, 0, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [2, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, 2],
     [2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 0, 2, 1, 0, 2, 0, 0, 0, 2, 2, 2, 0, 2, 0, 0],
     [2, 0, 0, 0, 2, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
     [2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 2, 0, 1],
     [0, 0, 0, 1, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 1, 2, 0],
     [0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 1, 0],
     [2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2],
     [2, 0, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 1, 0],
     [0, 0, 2, 2, 0, 0, 1, 2, 0, 0, 2, 1, 0, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 1],
     [0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 2, 1, 2, 2, 2, 2],
     [2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0, 2, 1, 0, 0, 0],
     [2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2],
     [0, 2, 1, 1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 1, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0],
     [2, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 1],
     [0, 2, 0, 0, 1, 2, 0, 0, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 2, 0, 2],
     [0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
     [2, 2, 2, 2, 2, 1, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0],
     [0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 1, 0],
     [2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 2],
     [0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0, 1, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 2, 2],
     [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 0, 2, 0, 0, 2],
     [0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 0, 2, 2, 0, 2, 1, 2, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 2, 2, 2, 0],
     [0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 0, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2],
     [0, 0, 0, 2, 0, 0, 0, 0, 1, 2, 0, 2, 2, 0, 2, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
     [0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 2, 0, 2, 2, 0, 0, 2, 2, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2],
     [1, 0, 2, 2, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 2, 2],
     [0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2],
     [2, 0, 0, 2, 2, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2],
     [2, 0, 0, 0, 1, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 1, 0, 2, 0, 2, 0, 2, 0, 2, 2, 0, 2, 1, 0, 0, 0]]
]
dout = [
    7,
    -1,
    5,
    -1
]

for i, expected in zip(din, dout):
    actual = shortest_distance(i)
    print(actual)
    print(expected)
    assert actual == expected
