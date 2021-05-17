"""
https://leetcode.com/problems/balance-a-binary-search-tree/ (MEDIUM)

Given a binary search tree, return a balanced binary search tree with the same node values.
A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.
If there is more than one answer, return any of them.


EXAMPLE 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        if root is None:
            return None

        def inorder_traversal(node: TreeNode) -> List[int]:
            sol = []
            if node.left is not None:
                sol = inorder_traversal(node.left)

            sol.append(node.val)

            if node.right is not None:
                sol.extend(inorder_traversal(node.right))

            return sol

        inorder = inorder_traversal(root)

        def construct_tree(nodes_list: List[int]) -> TreeNode:

            if len(nodes_list) == 0:
                return None

            if len(nodes_list) == 1:
                return TreeNode(nodes_list[0])

            if len(nodes_list) <= 3:
                left = TreeNode(nodes_list[0])
                root = TreeNode(nodes_list[1])
                root.left = left

                if len(nodes_list) == 3:
                    right = TreeNode(nodes_list[2])
                    root.right = right

                return root

            mid = len(nodes_list) // 2

            left = construct_tree(nodes_list[0:mid])
            right = construct_tree(nodes_list[mid + 1:])
            root = TreeNode(nodes_list[mid])
            root.left = left
            root.right = right

            return root

        root = construct_tree(inorder)
        return root


# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.right = TreeNode(3)
# root.right.right.right = TreeNode(4)


root = TreeNode(1)
root.right = TreeNode(15)
root.right.right = TreeNode(17)
root.right.left = TreeNode(14)
root.right.left.left = TreeNode(7)
root.right.left.left.right = TreeNode(12)
root.right.left.left.left = TreeNode(2)
root.right.left.left.left.right = TreeNode(3)
root.right.left.left.right.left = TreeNode(9)
root.right.left.left.right.left.right = TreeNode(11)

s = Solution()
s.balanceBST(root)
