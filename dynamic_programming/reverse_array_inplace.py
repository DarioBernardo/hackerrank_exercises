orig = [14, 9, 67, 91, 101, 25]
a = orig.copy()
print(a)

# METHOD 1
# reverse first time
index = len(a)-2
while index >= 0:
    a.append(a.pop(index))
    index -= 1

print(a)


# METHOD 2: recursion
def reverse(arr) -> list:
    if len(arr) == 1:
        return arr

    subset = reverse(arr[1:])
    subset.append(arr[0])
    return subset


b = reverse(a)
print(b)

assert b == orig
