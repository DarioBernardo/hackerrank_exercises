"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
"""

prices = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1],
    [200, 500, 1000, 700, 30, 400, 900, 400, 50]
]

sol = [5, 0, 870]


def max_profit(price_list: list):
    """
    With recursion
    """
    if len(price_list) < 2:
        raise Exception("Not enough data")

    if len(price_list) == 2:
        return price_list[-1] - price_list[-2]

    current_max_profit = 0
    for i in range(1, len(price_list)):
        current_profit = price_list[i] - price_list[0]
        if current_profit > current_max_profit:
            current_max_profit = current_profit

    max_profit_in_sub_string = max_profit(price_list[1:])

    return max(current_max_profit, max_profit_in_sub_string)


for p, s in zip(prices, sol):
    print("SOL:")
    print(max_profit(p))
    print(s)
    assert max_profit(p) == s

