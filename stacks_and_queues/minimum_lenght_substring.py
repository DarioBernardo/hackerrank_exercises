"""
Minimum Length Substrings
You are given two strings s and t. You can select any substring of string s and rearrange the characters of the selected substring. Determine the minimum length of the substring of s such that string t is a substring of the selected substring.
Signature
int minLengthSubstring(String s, String t)
Input
s and t are non-empty strings that contain less than 1,000,000 characters each
Output
Return the minimum length of the substring of s. If it is not possible, return -1
Example
s = "dcbefebce"
t = "fd"'
output = 5
Explanation:
Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.
"""


def compare_dicts(a, b) -> bool:
    for k in b.keys():
        if k not in a:
            return False
        else:
            if b[k] > a[k]:
                return False

    return True


def min_length_substring(s, t):
    # Write your code here

    if len(s) == 0 or len(t) == 0:
        return 0

    control = s
    test = t
    if len(s) < len(t):
        test = s
        control = t

    if len(test) == 1:
        return 1 if test in control else 0

    results = []
    stack_index = []
    stack = []
    string_hash = {}
    test_hash = {}

    for c in test:
        char_counter = test_hash.get(c, 0)
        char_counter += 1
        test_hash[c] = char_counter

    for pos, c in enumerate(control):
        if c in test_hash.keys():
            stack.append(c)
            stack_index.append(pos)

            char_counter = string_hash.get(c, 0)
            char_counter += 1
            string_hash[c] = char_counter

            if compare_dicts(string_hash, test_hash):
                results.append(stack_index[-1] - stack_index[0] + 1)
                removed_elem = stack.pop(0)
                _ = stack_index.pop(0)
                string_hash[removed_elem] -= 1
                while string_hash[stack[0]] > 1:
                    removed_elem = stack.pop(0)
                    _ = stack_index.pop(0)
                    string_hash[removed_elem] -= 1
                if string_hash[removed_elem] <= 0:
                    del string_hash[removed_elem]

    if compare_dicts(string_hash, test_hash):
        results.append(stack_index[-1] - stack_index[0] + 1)

    return -1 if len(results) == 0 else min(results)


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
    print('[', n, ']', sep='', end='')


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
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "dcbefebce"
    t1 = "fd"
    expected_1 = 5
    output_1 = min_length_substring(s1, t1)
    check(expected_1, output_1)

    s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
    t2 = "cbccfafebccdccebdd"
    expected_2 = -1
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)

    # Add your own test cases here
    s3 = "abcdefghilmno"
    t3 = "gme"
    expected_3 = 7
    output_3 = min_length_substring(s3, t3)
    check(expected_3, output_3)

    s2 = "ambhicdefgmnbo"
    t2 = "gme"
    expected_2 = 4
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)

    s2 = "ambhicdefgmnboglkslkbtemg"
    t2 = "gme"
    expected_2 = 3
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)

    s6 = "ambhicdefgmnboglkslkbtmegdff"
    t6 = "gme"
    expected_6 = 3
    output_6 = min_length_substring(s6, t6)
    check(expected_6, output_6)
