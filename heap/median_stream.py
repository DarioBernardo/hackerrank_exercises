"""
Median Stream (difficult)
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the median of the elements arr[0..i] (rounded down to the nearest integer).
The median of a list of integers is defined as follows. If the integers were to be sorted, then:
If there are an odd number of integers, then the median is equal to the middle integer in the sorted order.
Otherwise, if there are an even number of integers, then the median is equal to the average of the two middle-most integers in the sorted order.
Signature
int[] findMedian(int[] arr)
Input
n is in the range [1, 1,000,000].
Each value arr[i] is in the range [1, 1,000,000].
Output
Return a list of n integers output[0..(n-1)], as described above.
Example 1
n = 4
arr = [5, 15, 1, 3]
output = [5, 10, 5, 4]
The median of [5] is 5, the median of [5, 15] is (5 + 15) / 2 = 10, the median of [5, 15, 1] is 5, and the median of [5, 15, 1, 3] is (3 + 5) / 2 = 4.
Example 2
n = 2
arr = [1, 2]
output = [1, 1]
The median of [1] is 1, the median of [1, 2] is (1 + 2) / 2 = 1.5 (which should be rounded down to 1).
"""

import math

# Add any extra import statements you may need here


# Add any helper functions you may need here


"""
heap = [1, 3, 5, 15]
"""


def swap(h: list, a: int, b: int):
    temp = h[a]
    h[a] = h[b]
    h[b] = temp


def heapfy(h: list, e):
    if len(h) == 0:
        h.append(e)
    else:
        h.append(e)
        current = len(h) - 1
        previous = current - 1
        while previous >= 0 and h[previous] > h[current]:
            swap(h, current, previous)
            previous -= 1
            current -= 1


def findMedian(arr):
    # Write your code here
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr[0]

    heap = []
    result = []
    for elem in arr:
        heapfy(heap, elem)

        if len(heap) == 1:
            result.append(heap[0])
        elif len(heap) % 2 == 0:
            val = (heap[int(len(heap) / 2)] + heap[int(len(heap) / 2) - 1]) / 2
            result.append(int(val))
        else:
            index = int((len(heap) + 1) / 2) - 1
            result.append(heap[index])

    return result


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
    print('[', n, ']', sep='', end='')


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [5, 15, 1, 3]
    expected_1 = [5, 10, 5, 4]
    output_1 = findMedian(arr_1)
    check(expected_1, output_1)

    arr_2 = [2, 4, 7, 1, 5, 3]
    expected_2 = [2, 3, 4, 3, 4, 3]
    output_2 = findMedian(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
