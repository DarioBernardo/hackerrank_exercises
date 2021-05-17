"""
https://www.hackerrank.com/challenges/magic-square-forming/problem
"""

# !/bin/python3

import math
import os
import random
import re
import sys


def mapping(s) -> str:
    hash_str = "<"
    for sub_s in s:
        hash_str += "{}-{}-{}\n".format(sub_s[0], sub_s[1], sub_s[2])
    return hash_str[:-1] + ">"


def is_valid(arr) -> bool:
    if sum(arr[0]) == 15 and \
            sum(arr[1]) == 15 and \
            sum(arr[2]) == 15 and \
            arr[0][0] + arr[0][1] + arr[0][2] == 15 and \
            arr[1][0] + arr[1][1] + arr[1][2] == 15 and \
            arr[2][0] + arr[2][1] + arr[2][2] == 15 and \
            arr[0][0] + arr[1][0] + arr[2][0] == 15 and \
            arr[0][1] + arr[1][1] + arr[2][1] == 15 and \
            arr[0][2] + arr[1][2] + arr[2][2] == 15 and \
            arr[0][0] + arr[1][1] + arr[2][2] == 15 and \
            arr[0][2] + arr[1][1] + arr[2][0] == 15:
        return True

    return False


def possible_neighbours(arr) -> list:
    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    c_2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    permutations = []
    for row_num in range(0, 3):
        for col_num in range(0, 3):
            c[row_num][col_num] = arr[row_num][col_num] + 1
            c_2[row_num][col_num] = arr[row_num][col_num] - 1
            permutations.append(c)
            permutations.append(c_2)

    return permutations


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    # In any 3x3 square the magic constant is always 15

    if is_valid(s):
        return 0

    queue = [s]
    cost_map = {mapping(s): 0}

    while len(queue) != 0:
        current_square = queue.pop(0)
        current_cost = cost_map[mapping(current_square)]

        neighbours = possible_neighbours(current_square)

        for n in neighbours:
            if is_valid(n):
                return current_cost + 1
            else:
                if mapping(n) not in cost_map:
                    cost_map[mapping(n)] = current_cost + 1
                    queue.append(n)
                # elif cost_map[mapping(n[0])] > n[1]:
                #     cost_map[mapping(n[0])] = n[1]

    return -1


if __name__ == '__main__':

    s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
    result = formingMagicSquare(s)

    print(result)
