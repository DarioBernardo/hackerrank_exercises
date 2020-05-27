"""
Each array `x` is a user activity, at x[i] he made x transactions. Find out when he churned
Given a threshold `n` > 0, an user is considered churned when he has n consecutive zero elements in his activity array.
His lifespan is the length of the activity array until the first consecutive n number of zeros.
For example :
given the following array:
[3.0, 0.0, 9.0, 30.0, 7.0, 14.0, 0.0, 0.0, 5.0, 6.0, 11.0, 0.0, 9.0, 8.0, 2.0, 10.0, 0.0, 0.0, 0.0]
if threshold was 1 then lifespan is 1.
if threshold was 2 then lifespan is 6.
if threshold was 3 then lifespan is 19.
"""

a = [[3.0, 0.0, 9.0, 30.0, 7.0, 14.0, 0.0, 0.0, 5.0, 6.0, 11.0, 0.0, 9.0, 8.0, 2.0, 10.0, 0.0, 0.0, 0.0],
     [1.0, 0.0, 0.0, 0.0, 1.0, 4.0],
     [3.0, 0.0, 9.0, 30.0, 7.0, 14.0, 0.0, 0.0, 5.0, 6.0, 11.0, 0.0, 9.0, 8.0]]
out = [(19, False), (4, False), (14, True)]


def get_life_span(data, threshold=3):
    zeros_counter = 0
    for i, elem in enumerate(data, 1):
        if elem == 0:
            zeros_counter += 1
        else:
            zeros_counter = 0

        if zeros_counter == threshold:
            return i, False

    return len(data), True


for d, expected in zip(a, out):
    r = get_life_span(d)
    print(r)
    assert r == expected
