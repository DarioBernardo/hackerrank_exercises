"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""
from typing import List


def hash(i, j) -> str:
    return "{}-{}".format(i, j)


def get_children(x: int, y: int, x_max: int, y_max: int) -> list:
    children = []
    if x > 0:
        children.append((x - 1, y))
    if x < x_max:
        children.append((x + 1, y))

    if y > 0:
        children.append((x, y - 1))
    if y < y_max:
        children.append((x, y + 1))

    return children


def bfs(queue, visited_nodes, grid):
    x = len(grid)-1
    y = len(grid[0])-1
    while len(queue) > 0:
        elem = queue.pop(0)
        if hash(elem[0], elem[1]) not in visited_nodes:
            visited_nodes.add(hash(elem[0], elem[1]))
            children = get_children(elem[0], elem[1], x, y)
            for child in children:
                if grid[child[0]][child[1]] == "1":
                    queue.append(child)


def num_islands(grid: List[List[str]]) -> int:

    if len(grid) == 0:
        return 0
    if len(grid[0]) == 0:
        return 0
    if len(grid) == 1 and len(grid[0]) == 1:
        return 1 if grid[0][0] == "1" else "0"

    x = len(grid)
    y = len(grid[0])

    visited_nodes = set()
    island_counter = 0
    for xi in range(0, x):
        for yi in range(0, y):
            starting_point = grid[xi][yi]
            if hash(xi, yi) not in visited_nodes and starting_point == "1":
                island_counter += 1
                queue = [(xi, yi)]
                bfs(queue, visited_nodes, grid)

    return island_counter


din = [
    [["1", "1", "1", "1", "0"],
     ["1", "1", "0", "1", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "0", "0", "0"]],

    [["1", "1", "0", "0", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "1", "0", "0"],
     ["0", "0", "0", "1", "1"]]
]

expected_results = [
    1,
    3
]

for i, expected in zip(din, expected_results):
    actual = num_islands(i)
    print(actual)
    print(expected)
    assert actual == expected
