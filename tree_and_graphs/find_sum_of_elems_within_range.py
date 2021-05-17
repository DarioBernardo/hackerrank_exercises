"""
ACTUAL INTERVIEW QUESTION (22 March 2021)

given a binary search tree, find the sum of all elements that fall in the range [a, b] (inclusive).

Example 1:
        5
      /  \
    2     8
   / \     \
  1   3    10
range = [2, 4]

Output: 5
Explanation: the only nodes that fall between the range are 2 and 3. Their sum is 5

Note:
    Can you optimise time? do you need to traverse all tree? it is a binary search tree!
"""


class Node:
    def __init__(self, v: int, left: 'Node' = None, right: 'Node' = None):
        self.val = v
        self.right_child = right
        self.left_child = left


def find_sum(root: Node, low: int, up: int) -> int:

    if low > up:
        return 0

    def dfs(node: Node, low: int, up: int) -> int:

        sol = 0
        if node is None:
            return 0
        if low <= node.val <= up:
            sol += node.val

        if node.right_child is not None and not node.val > up:
            sol += dfs(node.right_child, low, up)

        if node.left_child is not None and not node.val < low:
            sol += dfs(node.left_child, low, up)

        return sol

    return dfs(root, low, up)


tree1 = Node(5)
tree1.right_child = Node(8)
tree1.right_child.right_child = Node(10)
tree1.left_child = Node(2)
tree1.left_child.right_child = Node(3)
tree1.left_child.left_child = Node(1)

actual = find_sum(tree1, 2, 4)
print(f"Result is: {actual}")
assert actual == 5

"""
Example 2:
        5
      /  \
    2     8
   / \   / \
  1   3  7 10
        / /
        6 9
range = [6, 9]
"""

tree1 = Node(5)
tree1.right_child = Node(8)
tree1.right_child.left_child = Node(7)
tree1.right_child.left_child.left_child = Node(6)
tree1.right_child.right_child = Node(10)
tree1.right_child.right_child.left_child = Node(9)
tree1.left_child = Node(2)
tree1.left_child.right_child = Node(3)
tree1.left_child.left_child = Node(1)

actual = find_sum(tree1, 6, 9)
print(f"Result is: {actual}")
assert actual == 30
