class Graph(object):
    def __init__(self, n_nodes, cost: int = 6):
        self.n_size = n_nodes
        self.nodes = {}
        self.connection_cost = cost

    def __make_directed_connection(self, s, d):
        s_connections = self.nodes.get(s, [])
        s_connections.append(d)
        self.nodes[s] = s_connections

    def connect(self, n1, n2):
        self.__make_directed_connection(n1, n2)
        self.__make_directed_connection(n2, n1)

    def find_all_distances(self, start_node):
        res = []
        for dest in range(1, self.n_size + 1):
            if dest != start_node:
                distance = self.bfs(start_node, dest)
                res.append(distance)

        # msg = ""
        # for d in range(0, len(res) - 1):
        #     msg += str(res[d]) + " "
        #
        # msg += str(res[len(res) - 1])
        # print(msg)
        return res

    """
    current_cost = 12
    queue [4 4]
    visited [2 3 4] 
    next_batch = []
    """

    def bfs(self, s, e):
        visited_nodes = set()
        queue = self.nodes[s].copy()
        current_cost = 0

        next_batch = self.nodes[s].copy()
        while len(next_batch) > 0:
            queue = next_batch
            next_batch = []
            current_cost += self.connection_cost

            for elem in queue:
                if elem not in visited_nodes:
                    if elem == e:
                        return current_cost
                    else:
                        visited_nodes.add(elem)
                        next_batch.extend(self.nodes[elem].copy())

        return -1


graph_sizes = [6, 4]
connections = [
    [
        [1, 2],
        [1, 3],
        [2, 4],
        [3, 4],
        [4, 5]
    ],
    [
        [1, 3],
        [1, 2],
        [2, 4]
    ]

]
solutions = [
    [6, 6, 12, 18, -1],
    [6, 6, 12]
]

for i, s in enumerate(graph_sizes):
    graph = Graph(s)
    for c in connections[i]:
        graph.connect(c[0], c[1])

    costs = graph.find_all_distances(1)
    print(costs)
    assert costs == solutions[i]

print("CORRECT!")
