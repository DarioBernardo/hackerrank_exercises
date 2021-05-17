"""
Element Swapping
Given a sequence of n integers arr, determine the lexicographically smallest sequence which may be obtained from it after performing at most k element swaps, each involving a pair of consecutive elements in the sequence.
Note: A list x is lexicographically smaller than a different equal-length list y if and only if, for the earliest index at which the two lists differ, x's element at that index is smaller than y's element at that index.
Signature
int[] findMinArray(int[] arr, int k)
Input
n is in the range [1, 1000].
Each element of arr is in the range [1, 1,000,000].
k is in the range [1, 1000].
Output
Return an array of n integers output, the lexicographically smallest sequence achievable after at most k swaps.
Example 1
n = 3
k = 2
arr = [5, 3, 1]
output = [1, 5, 3]
We can swap the 2nd and 3rd elements, followed by the 1st and 2nd elements, to end up with the sequence [1, 5, 3]. This is the lexicographically smallest sequence achievable after at most 2 swaps.
Example 2
n = 5
k = 3
arr = [8, 9, 11, 2, 1]
output = [2, 8, 9, 11, 1]
We can swap [11, 2], followed by [9, 2], then [8, 2].
"""

# Add any helper functions you may need here
def swap(source: int, destination: int, arr: list):
    temp = arr[source]
    arr[source] = arr[destination]
    arr[destination] = temp


def findMinArray(arr, k):
    # Write your code here

    if len(arr) == 0:
        return []
    if k == 0:
        return arr.copy()
    if k == 1:
        if arr[0] < arr[1]:
            return arr.copy()
        else:
            swap(0, 1, arr)
            return arr.copy()

    """
    [1, 5, 3]
    k = 2
  
    swaps_counter = 2
    index_of_min = 0
    min_val = 1
    """

    index_of_min = -1
    min_val = 1100000
    for i in range(0, min(k + 1, len(arr))):
        if min_val > arr[i] or index_of_min < 0:
            min_val = arr[i]
            index_of_min = i

    swaps_counter = 0
    while index_of_min > 0 and swaps_counter < k:
        swap(index_of_min, index_of_min - 1, arr)
        index_of_min -= 1
        swaps_counter += 1

    spare_iterations = k - swaps_counter
    if spare_iterations > 0:
        arr[1:] = findMinArray(arr[1:], spare_iterations)

    return arr


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
    n_1 = 3
    arr_1 = [5, 3, 1]
    k_1 = 2
    expected_1 = [1, 5, 3]
    output_1 = findMinArray(arr_1, k_1)
    check(expected_1, output_1)

    n_2 = 5
    arr_2 = [8, 9, 11, 2, 1]
    k_2 = 3
    expected_2 = [2, 8, 9, 11, 1]
    output_2 = findMinArray(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here
    n_3 = 5
    arr_3 = [2, 9, 8, 11, 1]
    k_3 = 3
    expected_3 = [2, 1, 9, 8, 11]
    output_3 = findMinArray(arr_3, k_3)
    check(expected_3, output_3)
