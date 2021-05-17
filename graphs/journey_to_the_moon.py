"""
medium
https://www.hackerrank.com/challenges/journey-to-the-moon/problem
"""


class GraphMap:
    def __init__(self):
        self.graph_map = dict()

    def add_link(self, a, b):
        links = self.children_of(a)
        links.append(b)
        self.graph_map[a] = links

    def add_bidirectional_link(self, a, b):
        self.add_link(a, b)
        self.add_link(b, a)

    def children_of(self, a):
        return self.graph_map.get(a, [])


def size_of_parent_graph(astronaut, gm, visited_astronauts):
    queue = [astronaut]
    graph_size = 0
    while len(queue) != 0:
        a = queue.pop(0)
        if a not in visited_astronauts:
            visited_astronauts.add(a)
            graph_size += 1
            children = gm.children_of(a)
            queue.extend(children)

    return graph_size


# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    if n <= 1:
        return 0

    graph_map = GraphMap()
    for pair in astronaut:
        graph_map.add_bidirectional_link(pair[0], pair[1])

    # find unique separate graphs
    country_sizes = []
    visited_astronauts = set()
    for a in range(0, n):
        if a not in visited_astronauts:
            country_size = size_of_parent_graph(a, graph_map, visited_astronauts)
            country_sizes.append(country_size)

    total = 0
    my_result = 0
    for size in country_sizes:
        my_result += total * size
        total += size

    return my_result


data_in = [
    (5, [(0, 1), (2, 3), (0, 4)]),
    (4, [(0, 2)]),
    (10, [(0, 2), (1, 8), (1, 4), (2, 8), (2, 6), (3, 5), (6, 9)])
]

expected_outputs = [6, 5, 23]

test_case_number = 1
for (tot_number_of_astronauts, astronauts_pairs), expected in zip(data_in, expected_outputs):
    actual = journeyToMoon(tot_number_of_astronauts, astronauts_pairs)

    result = actual == expected

    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        print(expected, end='')
        print(' Your output: ', end='')
        print(actual)
        print()
    test_case_number += 1
