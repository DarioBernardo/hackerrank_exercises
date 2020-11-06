"""
https://www.hackerrank.com/challenges/mini-max-sum/

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Return the respective minimum and maximum values as tuple of integers.

Example

arr = [1, 3, 5, 7, 9]
The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24.
The function returns: (16, 24)

"""

input_outputs = [([1, 3, 5, 7, 9], (16, 24)),
                 ([1, 2, 3, 4, 5], (10, 14)),
                 ([7, 69, 2, 221, 8974], (299, 9271))]


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    vals = []
    tot = sum(arr)
    for elem in arr:
        vals.append(tot - elem)

    return min(vals), max(vals)


for i, o in input_outputs:
    actual = miniMaxSum(i)
    assert actual == o
