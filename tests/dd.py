import numpy as np


class Node(object):

    def __init__(self, value):
        self.value = value
        # print(f"creating node with value {self.value}")
        self.children = []

    def add_child(self, value):
        if len(self.children) == 2:
            raise Exception(f"Can't add more children here! {len(self.children)}")

        self.children.append(Node(value))

    def get_children(self):
        return self.children


def get_bfs_level_avg(tree_head: Node) -> dict:

    def _update_result(result, level, children):
        children_for_level = result.get(level, [])
        for child in children:
            children_for_level.append(child.value)

        result[level] = children_for_level

    result = {}
    level = 1
    queue = [tree_head]

    while len(queue) != 0:

        _update_result(result, level, queue)

        new_queue = []
        for elem in queue:
            new_queue.extend(elem.get_children())

        queue = new_queue
        level += 1

    avgs = {}
    for key, value in result.items():
        avgs[key] = np.mean(value)

    return avgs


def get_dfs_level_avg(tree_head: Node) -> dict:
    result = {}
    level = 1

    def _update_result(result, level, child):
        children_for_level = result.get(level, [])
        children_for_level.append(child.value)
        result[level] = children_for_level

    def _collect(level: int, node: Node, result):
        for child in node.children:
            _collect(level+1, child, result)

        _update_result(result, level, node)

    _collect(level, tree_head, result)

    avgs = {}
    for key, value in result.items():
        avgs[key] = np.mean(value)

    return avgs


th = Node(4)
th.add_child(7)
th.add_child(9)
th.get_children()[1].add_child(6)
th.get_children()[0].add_child(10)
th.get_children()[0].add_child(2)
th.get_children()[0].get_children()[1].add_child(6)
th.get_children()[0].get_children()[1].get_children()[0].add_child(2)
avgs = get_bfs_level_avg(th)
print(avgs)

avgs = get_dfs_level_avg(th)
s = sorted(avgs.items(), key=lambda x: x[0])
print(s)
print(avgs)


