# Fibonacci calculator with accumulator


def fibo(n: int) -> int:
    accumulator = {}

    def calculate_fibonacci(val: int) -> int:
        if val == 1 or val == 0:
            return 1

        saved_res = accumulator.get(val, None)
        if saved_res is not None:
            return saved_res

        res = calculate_fibonacci(val-1) + calculate_fibonacci(val-2)
        accumulator[val] = res
        return res

    return calculate_fibonacci(n)


def fibo_dynamic(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    """
    f(n) = f(n-1) + f(n-2)
    """
    stack = [1, 1]
    for i in range(2, n):
        stack.append(stack[-2] + stack[-1])

    return stack[-2] + stack[-1]


vals = {8: 34,
        9: 55, 10: 89,
        11: 144,
        12: 233,
        98: 218922995834555169026,
        99: 354224848179261915075,
        100: 573147844013817084101,
        101: 927372692193078999176,
        102: 1500520536206896083277
        }
for key, val in vals.items():
    fibo_val = fibo(key)
    d_fibo_val = fibo_dynamic(key)

    print(f"Fibonacci of {key} is {fibo_val}")
    assert fibo_val == val
    assert d_fibo_val == val

import random

random_number = random.randint(50, 200)
fibo_val = fibo(random_number)
d_fibo_val = fibo_dynamic(random_number)
print(f"Fibonacci of {random_number} is {fibo_val}")
assert d_fibo_val == fibo_val
print("DONE!")
