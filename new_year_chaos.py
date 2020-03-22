"""
NEW YEAR CHAOS

https://www.hackerrank.com/challenges/new-year-chaos

"""


def shift(arr, src_index, dest_index):
    if src_index == dest_index or abs(src_index - dest_index) > 2:
        return

    if src_index - dest_index == 1:
        swap(arr, dest_index, src_index)
    else:
        swap(arr, dest_index, src_index)
        swap(arr, dest_index, src_index+1)


def swap(arr, dest_index, src_index):
    temp = arr[src_index]
    arr[src_index] = arr[dest_index]
    arr[dest_index] = temp


def minimumBribes(q):
    tot_bribes = 0
    state = list(range(1, len(q)+1))
    for index, elem in enumerate(q):
        bribe = 0
        while elem != state[index+bribe] and bribe < 3:
            bribe += 1

        if bribe >= 3:
            print("Too chaotic")
            return
        if bribe > 0:
            shift(state, index, index+bribe)
            tot_bribes += bribe

    print(f"Bribes: {tot_bribes}")
    return tot_bribes


q = [2, 1, 5, 3, 4]
bribes = minimumBribes(q)
assert bribes == 3

q = [1, 2, 5, 3, 7, 8, 6, 4]
"""
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 5, 4, 6, 7, 8]
[1, 2, 5, 3, 4, 6, 7, 8]
[1, 2, 5, 3, 4, 7, 6, 8]
[1, 2, 5, 3, 7, 4, 6, 8]
[1, 2, 5, 3, 7, 4, 8, 6]
[1, 2, 5, 3, 7, 8, 4, 6]
[1, 2, 5, 3, 7, 8, 6, 4]
"""
bribes = minimumBribes(q)
assert bribes == 7

