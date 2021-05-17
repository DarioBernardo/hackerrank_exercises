# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, node, current_dept=0):
        if not node.left and not node.right:
            return current_dept

        left_depth = 0
        if node.left:
            left_depth = self.max_depth(node.left, current_dept + 1)

        right_depth = 0
        if node.right:
            right_depth = self.max_depth(node.right, current_dept + 1)

        self.ans = max(right_depth - current_dept + left_depth - current_dept, self.ans)

        return max(right_depth, left_depth)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.ans = 0

        if not root:
            return 0

        tree_max_depth = self.max_depth(root)

        return self.ans


r = TreeNode(1, None, TreeNode(1, None, None))
expected = 1

s = Solution()
actual = s.diameterOfBinaryTree(r)

print(actual)
