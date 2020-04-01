# Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.

data_in = [
    [3, 7, 4, 6, 5],
    [2, 1, 5, 8, 4],
    [3, 5, -7, 8, 10],
    [1, 3, 5, 2, 5, 3, 6, -3, 11, 25, 12, 3, 18, 7],
]

results = [13, 11, 15, 60]


cached_result = {}

# RECURSIVE VERSION
# def maxSubsetSum(arr):
#     if len(arr) == 1:
#         return arr[0]
#
#     if len(arr) == 2:
#         return max(arr[0], arr[1])
#
#     if len(arr) == 3:
#         return max(arr[0], arr[1], arr[0]+arr[2])
#
#     cached_max = cached_result.get(tuple(arr), None)
#     if cached_max:
#         print(f"cached called on {arr}, max is {cached_max}")
#         return cached_max
#
#     max_sum_range = arr[0]
#     for i in range(0, len(arr)-3):
#         elem = arr[i]
#         sub_set = arr[i+2:]
#         subset_max = maxSubsetSum(sub_set)
#         max_sum_range = max(max_sum_range, elem, subset_max, elem+subset_max)
#
#     cached_result[tuple(arr)] = max_sum_range
#     return max_sum_range


def maxSubsetSum(arr):
    dp = []
    dp.append(arr[0])
    dp.append(max(arr[:2]))
    ans = max(dp)
    for a in arr[2:]:
        dp.append(max(dp[-2]+a, a, ans))
        ans = max(ans, dp[-1])
    return ans


for d, s in zip(data_in, results):
    my_sol = maxSubsetSum(d)
    print(my_sol)
    assert my_sol == s
