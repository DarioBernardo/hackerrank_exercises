"""
MEDIUM
https://www.hackerrank.com/challenges/find-the-nearest-clone/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

"""


def find_shortest(graph_from, graph_to, ids, val):
    graph = dict()
    for node, sister in zip(graph_from, graph_to):
        siblings = graph.get(node, [])
        siblings.append(sister)
        graph[node] = siblings

        siblings = graph.get(sister, [])
        siblings.append(node)
        graph[sister] = siblings

    nodes_color = []
    for node_id, color in enumerate(ids, 1):
        if color == val:
            nodes_color.append(node_id)

    shortest_distance = None
    for root in nodes_color:
        queue = [(root, 0)]
        visited = set()

        while len(queue) > 0:
            node, current_distance = queue.pop(0)
            if node not in visited:
                visited.add(node)
                siblings = graph.get(node, [])

                for sister in siblings:
                    if sister not in visited:
                        if ids[sister - 1] == val:
                            if shortest_distance is None or shortest_distance > current_distance + 1:
                                shortest_distance = current_distance + 1
                        else:
                            queue.append((sister, current_distance + 1))

    if shortest_distance is not None:
        return shortest_distance

    return -1


din = [
    ([1, 1, 2, 3], [2, 3, 4, 5], [1, 2, 3, 3, 2], 2),
]

dout = [
    3
]


for data_in, expected in zip(din, dout):
    actual = find_shortest(data_in[0], data_in[1], data_in[2], data_in[3])
    print(f"Result is: {actual} expected {expected}")
    assert actual == expected
