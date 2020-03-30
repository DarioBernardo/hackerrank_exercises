import unittest
from exercises.tree_and_graphs.bfsshortreach import bfs


class Tester(unittest.TestCase):

    def test_simple1(self):
        edges = [[1, 2], [1, 3]]
        n = 4
        m = 2
        s = 1
        res, costs = bfs(n, m, edges, s)
        print(res)
        print(costs)
        # self.assertEqual(res, [6, 6, -1])
        self.assertEqual(res, [True, True, False])

    def test_simple2(self):
        edges = [[2, 3]]
        n = 3
        m = 1
        s = 2
        res, costs = bfs(n, m, edges, s)
        print(res)
        print(costs)
        # self.assertEqual(res, [6, 6, -1])
        self.assertEqual(res, [False, True])

    def test_simple3(self):
        edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]]
        n = 5
        m = 5
        s = 1
        res, costs = bfs(n, m, edges, s)
        print(res)
        print(costs)
        # self.assertEqual(res, [6, 6, -1])
        self.assertEqual(res, [True, True, True, True])

    def test_simple4(self):
        edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]]
        n = 6
        m = 5
        s = 1
        res, costs = bfs(n, m, edges, s)
        print(res)
        print(costs)
        # self.assertEqual(res, [6, 6, -1])
        self.assertEqual(res, [True, True, True, True, False])

    def test_simple5(self):
        edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [6, 7]]
        n = 7
        m = 5
        s = 1
        res, costs = bfs(n, m, edges, s)
        print(res)
        print(costs)
        # self.assertEqual(res, [6, 6, -1])
        self.assertEqual(res, [True, True, True, True, False, False])

    def test_simple6(self):
        n = 10
        m = 6
        s = 3
        edges = [[3, 1], [10, 1], [10, 1], [3, 1], [1, 8], [5, 2]]
        res, costs = bfs(n, m, edges, s)
        print(res)
        print(costs)
        # self.assertEqual(res, [6, 6, -1])
        self.assertEqual([6, -1, -1, -1, -1, -1, 12, -1, 12], costs)