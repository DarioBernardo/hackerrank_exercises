"""
ALIEN DICTIONARY (HARD)
https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/3025/

Example of topological sort exercise.
There is a new alien language that uses the English alphabet. However, the order among letters are unknown to you.

You are given a list of strings words from the dictionary, where words are sorted lexicographically by the rules of this new language.

Derive the order of letters in this language, and return it. If the given input is invalid, return "". If there are multiple valid solutions, return any of them.


Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""
from typing import List, Tuple


def get_association(a: str, b: str):
    for ca, cb in zip(a, b):
        if ca != cb:
            return ca, cb

    if len(a) > len(b):
        return -1
    return ""


def alien_order(words: List[str]) -> str:

    if len(words) == 0:
        return ""
    if len(words) == 1:
        return words[0]
    if len(words[0][0]) == 0:
        return ""

    associations_map = dict()
    indegree_count = dict()

    for i in range(0, len(words)):
        if i < len(words) - 1:
            association = get_association(words[i], words[i + 1])
            if association == -1:
                return ""

            if association != "":
                children = associations_map.get(association[0], [])
                children.append(association[1])
                associations_map[association[0]] = children

                counter = indegree_count.get(association[1], 0)
                indegree_count[association[1]] = counter + 1

        for c in set(words[i]):
            counter = indegree_count.get(c, 0)
            indegree_count[c] = counter

    queue = []
    seen = set()
    for letter, counter in indegree_count.items():
        if counter == 0:
            queue.append(letter)

    sol = ""
    while len(queue) != 0:
        node = queue.pop(0)
        seen.add(node)
        sol += node

        children = associations_map.get(node, [])
        for child in children:
            indegree_count[child] -= 1
            if indegree_count[child] == 0 and child not in seen:
                queue.append(child)

    if len(indegree_count) - len(seen) > 0:
        return ""

    return sol


words_in = [
    ["wrt", "wrf", "er", "ett", "rftt"],
    ["z", "x"],
    ["z", "x", "z"],
    ["z", "z"],
    ["zy", "zx"]
]

sols = [
    "wertf",
    "zx",
    "",
    "z",
    "yzx"
]


for i, expected in zip(words_in, sols):
    actual = alien_order(i)
    print(actual)
    assert actual == expected
