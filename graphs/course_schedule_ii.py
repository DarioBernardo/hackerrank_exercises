"""
MEDIUM
https://leetcode.com/problems/course-schedule-ii/

There are a total of n courses you have to take labelled from 0 to n - 1.
Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.
Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
So the correct course order is [0,1].


Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].


Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
"""

"""
The solution uses dfs to explore the graph, but also two sets, one for visited nodes 
and one for currently explored nodes which is used to detect cycles.
"""
from typing import List


def find_order(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    def dfs(n, g, visited, explored) -> List:
        children = g.get(n, [])

        if len(children) == 0:
            visited.add(n)
            return [n]

        explored.add(n)

        sol = []
        for child in children:
            if child in explored:
                raise Exception()
            if child not in visited:
                child_sol = dfs(child, g, visited, explored)
                sol.extend(child_sol)

        explored.remove(n)
        visited.add(n)
        sol.append(n)
        return sol

    graph = dict()
    visited = set()

    for p in prerequisites:
        children = graph.get(p[0], [])
        children.append(p[1])
        graph[p[0]] = children

    sol = []
    try:
        for n in range(0, numCourses):
            if n not in visited:
                currently_explored = set()
                this_n_deps = dfs(n, graph, visited, currently_explored)
                sol.extend(this_n_deps)
    except:
        return []

    return sol


din = [
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
    (2, [[1, 0]]),
    (7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]])
]

dout = [
    [0, 1, 2, 3],  # Also [0, 2, 1, 3] is valid
    [0, 1],
    [6, 5, 4, 2, 3, 0, 1]
]


for data_in, expected_result in zip(din, dout):
    actual_result = find_order(data_in[0], data_in[1])
    print(f"Expected: {expected_result}   Actual: {actual_result}")
    assert expected_result == actual_result
