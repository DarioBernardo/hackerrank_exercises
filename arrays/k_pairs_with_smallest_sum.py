"""
(MEDIUM) Find K Pairs with Smallest Sums
https://www.programcreek.com/2015/07/leetcode-find-k-pairs-with-smallest-sums-java/

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.
Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.


Example:

Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
"""

from typing import List

"""
[1,7,11]
[2,4,6]

sol = [[1,2], [1, 4], [1,6], [7,2], [7,4]]
pointer1 = 1
pointer2 = 1
"""
import math


def k_smallest_pairs(arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:

    if k > len(arr1) * len(arr2):
        k = len(arr1) * len(arr2)

    n1 = len(arr1)
    n2 = len(arr2)

    # Stores current index in arr2[] for
    # every element of arr1[]. Initially
    # all values are considered 0.
    # Here current index is the index before
    # which all elements are considered as
    # part of output.
    index2 = [0 for i in range(n1)]

    sol = []
    while k > 0:
        # Initialize current pair sum as infinite
        min_sum = math.inf
        min_index = 0

        # To pick next pair, traverse for all elements
        # of arr1[], for every element, find corresponding
        # current element in arr2[] and pick minimum of
        # all formed pairs.
        for i1 in range(0, n1, 1):
            # Check if current element of arr1[] plus
            # element of array2 to be used gives minimum
            # sum
            if index2[i1] < n2 and arr1[i1] + arr2[index2[i1]] <= min_sum:
                # Update index that gives minimum
                min_index = i1

                # update minimum sum
                min_sum = arr1[i1] + arr2[index2[i1]]

        sol.append([arr1[min_index], arr2[index2[min_index]]])

        index2[min_index] += 1

        k -= 1

    return sol


def printList(n):
    # print('[', n, ']', sep='', end='')
    print(n)


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='\n')
        printList(expected)
        print(' Your output: ', end='\n')
        printList(output)
        print()
    test_case_number += 1


arr_1 = [1, 7, 11]
arr_2 = [2, 4, 6]
expected_1 = [[1, 2], [1, 4], [1, 6]]
k = 3
output_1 = k_smallest_pairs(arr_1, arr_2, k)
check(expected_1, output_1)

arr_1 = [1, 7, 11]
arr_2 = [2, 4, 6]
expected_2 = [[1, 2], [1, 4], [1, 6], [7, 2], [7, 4], [11, 2], [7, 6], [11, 4], [11, 6]]
k = 9
output_2 = k_smallest_pairs(arr_1, arr_2, k)
check(expected_2, output_2)

# Add your own test cases here
arr_1 = [1, 7, 11]
arr_2 = [2, 4, 6]
expected_3 = [[1, 2], [1, 4], [1, 6], [7, 2], [7, 4], [11, 2], [7, 6], [11, 4], [11, 6]]
k = 12
output_3 = k_smallest_pairs(arr_1, arr_2, k)
check(expected_3, output_3)