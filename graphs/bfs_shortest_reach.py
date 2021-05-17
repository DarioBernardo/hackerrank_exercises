"""
https://www.hackerrank.com/challenges/bfsshortreach/problem
"""


def add_connection(graph, source, destination):
    list_of_childs = graph.get(source, [])
    list_of_childs.append(destination)
    graph[source] = list_of_childs


def bfs_algo(graph: dict, start: int, end: int) -> int:
    queue = [(start, 0)]
    visited = set()

    while len(queue) != 0:
        node, cost = queue.pop(0)
        if node == end:
            return cost
        if node not in visited:
            visited.add(node)
            children = graph[node]
            for child in children:
                if child not in visited:
                    queue.append((child, cost + 6))

    return -1


# Complete the bfs function below.
def bfs(n, m, edges, s):
    graph = dict()

    for e in edges:
        add_connection(graph, e[0], e[1])
        add_connection(graph, e[1], e[0])

    if s not in graph:
        return [-1] * len(edges)

    result = []
    for node in range(1, m + 1):
        if node != s:
            result.append(bfs_algo(graph, s, node))

    return result


data_in = [
    {"edges": [[1, 2], [1, 3]], "nodes": 4, "start": 1}
]

expected_out = [[6, 6, -1]]

for din, expected in zip(data_in, expected_out):
    actual = bfs(None, din["nodes"], din["edges"], din["start"])
    print(actual)
    print(expected)
