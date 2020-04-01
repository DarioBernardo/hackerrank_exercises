"""
Topological Sort: A topological sort or topological ordering of a directed graph is a linear ordering
of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
A topological ordering is possible if and only if the graph has no directed cycles, that is,
if it is a directed acyclic graph (DAG).

https://algorithms.tutorialhorizon.com/topological-sort/
https://algorithms.tutorialhorizon.com/determine-the-order-of-tests-when-tests-have-dependencies-on-each-other/

Test Cases: A B C D E F G
E depends on B, D, G
D depends on B, C
C depends on A
B depends on A
F no dependency
G depends on A

Output: Test Case sequence: F A B C D E
"""

nodes = ["A", "B", "C", "D", "E", "F", "G"]

dependencies = {"E": ["B", "D", "G"],
                "D": ["B", "C"],
                "C": ["A"],
                "B": ["A"],
                "F": [],
                "G": ["A", "D"]}

expected_output = ["A", "B", "C", "D", "G", "E", "F"]


def bfs(start, g: dict, dep: dict, print_list: list, visited_nodes: set):
    queue = [start]
    while len(queue) > 0:
        node = queue.pop(0)
        if node not in visited_nodes:
            fathers = dep.get(node, [])
            has_unsatisfied_dependency = False
            for parent in fathers:
                if parent not in visited_nodes:
                    queue.append(node)
                    has_unsatisfied_dependency = True
                    break

            if not has_unsatisfied_dependency:
                visited_nodes.add(node)
                print_list.append(node)
                queue.extend(g.get(node, []))


def topological_sort(n, d) -> list:
    print_list = []
    graph = {}
    for child, dep in d.items():
        for parent in dep:
            children = graph.get(parent, [])
            children.append(child)
            graph[parent] = children

    starting_nodes = []
    for node in n:
        node_dep = d.get(node, None)
        if not node_dep:  # this node has no dependencies
            starting_nodes.append(node)

    print(graph)
    visited_nodes = set()
    for start in starting_nodes:
        bfs(start, graph, d, print_list, visited_nodes)

    return print_list


order_list = topological_sort(nodes, dependencies)
print(order_list)









