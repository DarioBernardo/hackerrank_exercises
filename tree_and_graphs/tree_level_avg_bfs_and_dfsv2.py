"""
Given a binary tree, get the average value at each level of the tree.
Explained here:
https://vimeo.com/357608978
pass fbprep
"""
from typing import List


class Node:
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None


def get_bfs(nodes: List[Node], result: list):
    if len(nodes) == 0:
        return

    current_level_values = []
    next_level_children = []
    for n in nodes:
        current_level_values.append(n.value)
        if n.left:
            next_level_children.append(n.left)
        if n.right:
            next_level_children.append(n.right)

    result.append(sum(current_level_values)/len(current_level_values))
    get_bfs(next_level_children, result)


def get_dfs(n: Node, level_map: dict, current_level: int = 0):
    this_level_map = level_map.get(current_level, [])
    this_level_map.append(n.value)
    level_map[current_level] = this_level_map

    if n.left:
        get_dfs(n.left, level_map, current_level+1)
    if n.right:
        get_dfs(n.right, level_map, current_level+1)


def get_level_average(head: Node) -> list:
    if head is None:
        return []

    level_map = {}
    get_dfs(head, level_map)

    result = []
    levels = sorted(level_map.keys())
    for level in levels:
        level_values = level_map[level]
        result.append(sum(level_values)/len(level_values))

    return result


def get_level_average_2(head: Node) -> list:
    if head is None:
        return []

    result = []
    get_bfs([head], result)

    return result


th = Node(4)
th.left = Node(7)
th.right = Node(9)
th.right.right = Node(6)
th.left.left = Node(10)
th.left.right = Node(2)
th.left.right.right = Node(6)
th.left.right.right.left = Node(2)
expected = [4, 8, 6, 6, 2]

actual = get_level_average(th)
actual_bfs = get_level_average_2(th)

print("ACTUAL:  \t{}".format(actual))
print("EXPECTED:\t{}".format(expected))
assert actual == expected
assert actual_bfs == expected


root_2 = Node(10)
root_2.left = Node(8)
root_2.right = Node(15)
root_2.left.left = Node(3)
root_2.left.left.right = Node(5)
root_2.left.left.right.right = Node(6)
root_2.right.left = Node(14)
root_2.right.right = Node(16)
expected = [10.0, 11.5, 11, 5, 6]

actual = get_level_average(root_2)
actual_bfs = get_level_average_2(root_2)

print("ACTUAL:  \t{}".format(actual))
print("EXPECTED:\t{}".format(expected))
assert actual == expected
assert actual_bfs == expected

