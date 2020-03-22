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

    print(f"Fibonacci value for {key} is {fibo_val}")
    assert fibo_val == val