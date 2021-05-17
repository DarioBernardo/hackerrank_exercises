"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/ (HARD)

Serialization is the process of converting a data structure or object into a sequence of bits so that
it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized
to the original tree structure.
"""


# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs_preorder(node: TreeNode) -> List[int]:
    res = [node.val]

    if node.left is not None:
        res.extend(dfs_preorder(node.left))
    else:
        res.append(None)

    if node.right is not None:
        res.extend(dfs_preorder(node.right))
    else:
        res.append(None)

    return res


def dfs_construct(node, nums: List[int]):
    n = nums.pop(0)
    if n is not None:
        node.left = TreeNode(n)
        dfs_construct(node.left, nums)

    n = nums.pop(0)
    if n is not None:
        node.right = TreeNode(n)
        dfs_construct(node.right, nums)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return ""

        serialisation_list = dfs_preorder(root)
        return ",".join([str(x) for x in serialisation_list])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        raw_numbers = []
        for s in data.split(","):
            if s == "None":
                raw_numbers.append(None)
            else:
                raw_numbers.append(int(s))

        root = TreeNode(raw_numbers.pop(0))
        dfs_construct(root, raw_numbers)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# [1,2,3,null,null,4,5,6,7]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)


ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
print(ans)