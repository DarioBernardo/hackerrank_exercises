import numpy as np
import random


class Node:

    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def add_child(self, node):
        if node is None:
            return
        if node.value < self.value:
            self.add_left_child(node)
        else:
            self.add_right_child(node)

    def add_right_child(self, child):
        if child is None:
            return
        if self.right_child is None:
            self.right_child = child
        else:
            self.right_child.add_child(child)

    def add_left_child(self, child):
        if child is None:
            return
        if self.left_child is None:
            self.left_child = child
        else:
            self.left_child.add_child(child)

    def in_order_traversal(self):
        left = []
        if self.left_child is not None:
            left = self.left_child.in_order_traversal()
        left.append(self.value)
        if self.right_child is not None:
            right = self.right_child.in_order_traversal()
            left.extend(right)
        return left.copy()

    def rotate_right(self):
        if self.left_child is None:
            return self
        new_root = self.left_child
        self.left_child = None
        self.add_child(new_root.right_child)
        new_root.right_child = self
        return new_root

    def rotate_left(self):
        if self.right_child is None:
            return self
        new_root = self.right_child
        self.right_child = None
        self.add_child(new_root.left_child)
        new_root.left_child = self
        return new_root


ARRAY_LENGTH = 25

ROTATE_LEFT_PROBABILITY = 0.35
ROTATE_RIGHT_PROBABILITY = 0.4
PROB_DOUBLE = 0.2

print("Implementing spay trees! cool!")
my_pool = list(range(0, ARRAY_LENGTH * 2))
# print(my_pool)
my_array = sorted(np.random.choice(my_pool, ARRAY_LENGTH, replace=False))
print(my_array)

# my_array = [3, 5, 7, 9, 4, 8, 6, 1, 11, 10, 2, 25, 20]

current_state = []
root = None
for elem in my_array:
    current_state.append(elem)
    if root is None:
        root = Node(elem)
    else:
        root.add_child(Node(elem))

    if random.random() < ROTATE_LEFT_PROBABILITY:
        root = root.rotate_left()
        print("Rotated left.")
        if random.random() < PROB_DOUBLE:
            root = root.rotate_left()
            print("Double Rotated left.")
    if random.random() < ROTATE_LEFT_PROBABILITY:
        root = root.rotate_right()
        print("Rotated right.")
        if random.random() < PROB_DOUBLE:
            root = root.rotate_right()
            print("Double Rotated right.")

    assert sorted(current_state) == root.in_order_traversal()

print(root.in_order_traversal())
print("Worked perfectly!")