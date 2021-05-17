"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/ (MEDIUM)

We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node.
The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        sol = set()

        def dfs_childs(node: TreeNode, k: int, sol: set):

            if k == 0:
                sol.add(node.val)
                return

            if node.left is not None:
                dfs_childs(node.left, k - 1, sol)

            if node.right is not None:
                dfs_childs(node.right, k - 1, sol)

        def target_distance(node: TreeNode, t: TreeNode, k: int, sol: set) -> int:
            if node.val == t.val:
                return 0

            left_distance = -1
            if node.left is not None:
                left_distance = target_distance(node.left, t, k, sol)
                if left_distance >= 0:
                    left_distance += 1

            right_distance = -1
            if node.right is not None:
                right_distance = target_distance(node.right, t, k, sol)
                if right_distance >= 0:
                    right_distance += 1

            if left_distance - k == 0 or right_distance - k == 0:
                sol.add(node.val)

            if node.right is not None and left_distance > 0 and k - left_distance > 0:
                dfs_childs(node.right, k - left_distance - 1, sol)

            if node.left is not None and right_distance > 0 and k - right_distance > 0:
                dfs_childs(node.left, k - right_distance - 1, sol)

            return max(left_distance, right_distance)

        dfs_childs(target, K, sol)  # setting to sol target's children at distance k
        target_distance(root, target, K, sol)

        return list(sol)


# [3,5,1,6,2,0,8,null,null,7,4]

root = TreeNode(3)
root.right = TreeNode(1)
root.right.right = TreeNode(8)
root.right.left = TreeNode(0)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(4)
root.left.right.left = TreeNode(7)

s = Solution()
distance_k_nodes = s.distanceK(root, root.left, 2)
print(distance_k_nodes)

