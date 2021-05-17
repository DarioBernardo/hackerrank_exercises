"""
HARD
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).


"""
from typing import List


def get_children(n, m):
    vertical = []
    if n[0] > 0:
        vertical.append(n[0] - 1)
    if n[0] < len(m) - 1:
        vertical.append(n[0] + 1)

    horizontal = []
    if n[1] > 0:
        horizontal.append(n[1] - 1)
    if n[1] < len(m[0]) - 1:
        horizontal.append(n[1] + 1)

    childs = []
    for vd in vertical:
        childs.append((vd, n[1]))
    for hd in horizontal:
        childs.append((n[0], hd))

    return childs


def longestIncreasingPath(matrix: List[List[int]]) -> int:

    if len(matrix) == 0:
        return 0

    if len(matrix[0]) == 0:
        return 0

    def dfs(node, m: List[List[int]], visited):
        if node in visited:
            return visited[node]

        node_val = matrix[node[0]][node[1]]
        children = get_children(node, m)
        max_path = 1
        for child in children:
            child_val = matrix[child[0]][child[1]]
            if child_val > node_val:
                child_max_path = dfs(child, m, visited)
                if child_max_path + 1 > max_path:
                    max_path = child_max_path + 1

        visited[node] = max_path
        return max_path

    max_path = 0
    visited = dict()
    for h in range(0, len(matrix)):
        for v in range(0, len(matrix[0])):
            root = (h, v)
            if root not in visited:
                node_max_path = dfs(root, matrix, visited)
                if node_max_path > max_path:
                    max_path = node_max_path

                visited[root] = node_max_path

    return max_path


test_cases = [
    [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
]

solutions = [
    4
]

for test, sol in zip(test_cases, solutions):
    span = longestIncreasingPath(test)
    print(span)
    print(sol)
    assert span == sol
    print()

print("Done!")




