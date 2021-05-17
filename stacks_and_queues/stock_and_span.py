"""
Problem explained here:
https://practice.geeksforgeeks.org/problems/stock-span-problem/0

The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need
to calculate the span of stock’s price for all n days.
The span S(i) of the stock’s price on a given day i is defined as the maximum number of consecutive days just before
the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85},
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

solutions:
https://www.geeksforgeeks.org/the-stock-span-problem/
http://www.algorithmsandme.com/stacks-stock-span-problem/
"""

test_cases = [
    [100, 80, 60, 70, 60, 75, 85],
    [10, 4, 5, 90, 120, 80],
    [10, 20, 30, 40, 30, 20, 10],
    [60, 50, 40, 30, 20, 10, 100]
]

solutions = [
    [1, 1, 1, 2, 1, 4, 6],
    [1, 1, 2, 4, 5, 1],
    [1, 2, 3, 4, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 7]
]


def stock_and_span_v1(arr):

    stack = []
    weight = []
    result = []

    for stock in arr:
        current_stock_weight = 1
        while len(stack) > 0 and stock > stack[-1]:
            del stack[-1]
            current_stock_weight += weight[-1]
            del weight[-1]

        stack.append(stock)
        weight.append(current_stock_weight)
        result.append(current_stock_weight)

    return result


def stock_and_span(arr):
    # Adding -1 to consider when looking backwards since beginning,
    # and 0 because we initialise the first element result with span 1
    stack = [-1, 0]
    result = [1]

    for i in range(1, len(arr)):
        today_price = arr[i]
        while len(stack) > 1 and arr[stack[-1]] < today_price:
            del stack[-1]

        result.append(i-stack[-1])
        stack.append(i)

    return result


for test, sol in zip(test_cases, solutions):
    span = stock_and_span(test)
    print(span)
    print(sol)
    assert span == sol
    print()

print("Done!")
