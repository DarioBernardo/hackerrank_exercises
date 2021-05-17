"""
https://leetcode.com/explore/interview/card/facebook/54/sorting-and-searching-3/310/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 0:
        return []

    intervals = sorted(intervals, key=lambda tup: tup[0])

    start = intervals[0][0]
    end = intervals[0][1]

    result = []

    for i in range(1, len(intervals)):
        elem = intervals[i]

        if elem[0] <= end and elem[1] >= start:
            end = max(end, elem[1])
            start = min(start, elem[0])

        else:
            result.append([start, end])
            start = elem[0]
            end = elem[1]

    result.append([start, end])
    return result


din = [
    [[1, 3], [2, 6], [8, 10], [15, 18]],
    [[1, 4], [0, 2], [3, 5]],
    [[4, 5], [1, 4], [0, 1]]
]
dout = [
    [[1, 6], [8, 10], [15, 18]],
    [[0, 5]],
    [[0, 5]]
]

for i, expected in zip(din, dout):
    actual = merge(i)
    print(actual)
    print(expected)
    assert actual == expected
