"""
Balanced Split  (EASY/MEDIUM)
Given an array of integers (which may include repeated integers), determine if there's a way to split the array into two subsequences A and B such that the sum of the integers in both arrays is the same, and all of the integers in A are strictly smaller than all of the integers in B.
Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.
Signature
bool balancedSplitExists(int[] arr)
Input
All integers in array are in the range [0, 1,000,000,000].
Output
Return true if such a split is possible, and false otherwise.
Example 1
arr = [1, 5, 7, 1]
output = true
We can split the array into A = [1, 1, 5] and B = [7].
Example 2
arr = [12, 7, 6, 7, 6]
output = false
We can't split the array into A = [6, 6, 7] and B = [7, 12] since this doesn't satisfy the requirement that all integers in A are smaller than all integers in B.
"""


def balancedSplitExists(arr):
    # Write your code here

    if len(arr) <= 2:
        return False

    arr = sorted(arr)  # Timsort, time complexity O(n logn) in the worse case

    left = 0

    left_counter = arr[left]
    right_counter = 0

    last_elem_left = arr[left]
    first_elem_right = arr[left + 1]

    for i in range(left + 1, len(arr)):
        right_counter += arr[i]

    while left_counter <= right_counter:

        if left_counter == right_counter and last_elem_left != first_elem_right:
            return True

        left += 1

        if left + 1 >= len(arr):
            return False

        left_counter += arr[left]
        right_counter -= arr[left]

        last_elem_left = arr[left]
        first_elem_right = arr[left + 1]

    return False


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


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
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [2, 1, 2, 5]
    expected_1 = True
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)

    arr_2 = [3, 6, 3, 4, 4]
    expected_2 = False
    output_2 = balancedSplitExists(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
    arr_1 = [1, 5, 9, 1]
    expected_1 = False
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)

    arr_1 = [1, 5, 1]
    expected_1 = False
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)

    arr_1 = [1, 1]
    expected_1 = False
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)

    arr_1 = [1, 2]
    expected_1 = False
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)

    arr_1 = [1, 1, 2]
    expected_1 = True
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)