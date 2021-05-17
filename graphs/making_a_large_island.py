"""
https://leetcode.com/problems/making-a-large-island/  (HARD)

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.


Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.


Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.


Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

"""
from typing import Tuple, List


def get_children(node: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
    x = node[0]
    y = node[1]
    n = len(grid)

    x_coords = []
    if x > 0:
        x_coords.append(x - 1)
    if x < n - 1:
        x_coords.append(x + 1)

    y_coords = []
    if y > 0:
        y_coords.append(y - 1)
    if y < n - 1:
        y_coords.append(y + 1)

    children = []
    for xc in x_coords:
        children.append((xc, y))

    for yc in y_coords:
        children.append((x, yc))

    return children


def dfs(node: Tuple[int, int], grid: List[List[int]], nodes_group: dict, group: int) -> int:
    if node in nodes_group:
        return 0

    nodes_group[node] = group
    this_size = 1
    children = get_children(node, grid)
    for child in children:
        if grid[child[0]][child[1]] == 1:
            this_size += dfs(child, grid, nodes_group, group)

    return this_size


def visit(grid: List[List[int]]) -> Tuple[dict, dict]:
    nodes_group = dict()
    group_sizes = dict()
    group = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            elem = (i, j)
            if grid[i][j] == 1:
                group_size = dfs(elem, grid, nodes_group, group)
                group_sizes[group] = group_size
                group += 1

    return nodes_group, group_sizes


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        if len(grid) == 1:
            return 1

        islands_groups, islands_sizes = visit(grid)
        max_size = -1

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                elem = (i, j)
                if grid[i][j] == 0:
                    children = get_children(elem, grid)
                    groups_touched = dict()
                    for child in children:
                        if grid[child[0]][child[1]] == 1 and child in islands_groups:
                            child_group = islands_groups[child]
                            groups_touched[child_group] = islands_sizes[child_group]

                    this_elem_size = 1
                    for g, g_size in groups_touched.items():
                        this_elem_size += g_size

                    if this_elem_size > max_size:
                        max_size = this_elem_size

        if max_size == -1:
            return len(grid) * len(grid)

        return max_size


din = [
    [[1, 0], [0, 1]],
    [[1, 1], [1, 0]],
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
]

expected_out = [
    3,
    4,
    9
]

for i, expected in zip(din, expected_out):
    s = Solution()
    actual = s.largestIsland(i)
    print(actual)
    print(expected)
    assert actual == expected

