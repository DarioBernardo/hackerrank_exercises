# complexity is O(log n)


def search(nums: list, target: int):
    lo = 0
    hi = len(nums)-1

    while lo <= hi:
        pointer = (hi + lo) // 2
        if nums[pointer] == target:
            return pointer
        if nums[pointer] > target:
            hi = pointer - 1
        else:
            lo = pointer + 1

    return -1


a = [1, 2, 4, 5, 6, 7, 9, 11, 13, 14]
res = search(a, 2)
print(res)
assert res == 1

res = search(a, 11)
print(res)
assert res == 7

res = search(a, 8)
print(res)
assert res == -1

res = search(a, 0)
print(res)
assert res == -1

res = search([1, 3], 1)
print(res)
assert res == 0

res = search([1, 3], 3)
print(res)
assert res == 1