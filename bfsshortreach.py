class Node:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children = []

    def add_child(self, node: int):
        if not node in self.children:
            self.children.append(node)


# Complete the bfs function below.
def bfs(n, m, edges, s):
    visited_nodes = {}
    nodes = {}
    for node_id in range(1, n+1):
        nodes[node_id] = Node(node_id)

    for edge in edges:
        source = edge[0]
        destination = edge[1]
        nodes[source].add_child(destination)
        nodes[destination].add_child(source)

    result_founds = []
    result_costs = []
    for end_node in range(1, n+1):
        next_to_visit = nodes[s].children.copy()
        if end_node != s:
            for node_id in range(1, n + 1):
                visited_nodes[node_id] = False
            found = False
            cost = 6
            num_of_visits_before_increasing_cost = len(next_to_visit) - 1
            nephews_size = 0
            while len(next_to_visit) != 0:
                node_id = next_to_visit.pop(0)
                if end_node == node_id:
                    found = True
                    break

                for child in nodes[node_id].children:
                    if not visited_nodes[child]:
                        next_to_visit.append(child)
                    nephews_size = nephews_size + len(nodes[child].children)
                visited_nodes[node_id] = True

                if num_of_visits_before_increasing_cost == 0:
                    cost = cost + 6
                    num_of_visits_before_increasing_cost = nephews_size
                    nephews_size = 0
                num_of_visits_before_increasing_cost = num_of_visits_before_increasing_cost-1
            result_founds.append(found)
            if not found:
                result_costs.append(-1)
            else:
                result_costs.append(cost)

    return result_founds, result_costs


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        print("n = {}".format(n))
        print("m = {}".format(m))
        print("s = {}".format(s))
        print("edges = {}".format(edges))
