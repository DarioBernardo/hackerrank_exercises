"""
Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/ (HARD)

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.



Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.


Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""
from typing import List


def trap(height: List[int]) -> int:

    if len(height) <= 2:
        return 0

    if len(height) <= 2:
        return 0

    tot_area = 0
    stack = []

    for i, elem in enumerate(height):

        while len(stack) > 0 and elem >= height[stack[-1]]:
            prev_pos = stack.pop()
            if len(stack) == 0:
                break

            base = i - stack[-1] - 1
            bucket_height = min(elem, height[stack[-1]]) - height[prev_pos]
            tot_area += base * bucket_height

        stack.append(i)

    return tot_area

    # ans = 0
    # st = []
    #
    # for current in range(0, len(height)):
    #     while len(st) > 0 and height[current] > height[st[-1]]:
    #         top = st.pop()
    #         if len(st) == 0:
    #             break
    #
    #         distance = current - st[-1] - 1
    #         bounded_height = min(height[current], height[st[-1]]) - height[top]
    #         ans += distance * bounded_height
    #
    #     st.append(current)
    #
    # return ans


test_cases = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5],
    [5, 3, 2, 0, 4, 2, 6]
]

solutions = [
    6,
    9,
    14
]

for test, sol in zip(test_cases, solutions):
    span = trap(test)
    print(span)
    print(sol)
    assert span == sol
    print()

print("Done!")
