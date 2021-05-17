

def max_profit(prices: list):
        period = len(prices)
        buyDateIndex = 0
        tempIndex = 0
        sellDateIndex = 0
        current_profit = 0
        max_sell_price = prices[period - 1]  # assign the last element
        for i in range(period - 2, 0,  -1):
            if max_sell_price < prices[i]:
                max_sell_price = prices[i]
                tempIndex = i
            else:
                if max_sell_price > prices[i]:
                    if current_profit < max_sell_price - prices[i]:
                        current_profit = max_sell_price - prices[i]
                        buyDateIndex = i
                        sellDateIndex = tempIndex

        print("Maximum Profit(DP): {}, buy date index: {}, sell date index: {}"
              .format(current_profit, buyDateIndex, sellDateIndex))


prices = [200, 500, 1000, 700, 30, 400, 900, 400, 50]
max_profit(prices)

"""
buy 200 30
sell 1000 

daily = 2000

prifit  800
max_profit 800
"""


def max_profit_2(prices: list):
    if len(prices) <= 1:
        return 0

    min_index = 0
    max_profit = 0

    for i, price in enumerate(prices):
        if price <= prices[min_index]:
            min_index = i
        else:
            max_profit = max(max_profit, price - prices[min_index])

    return max_profit


val = max_profit_2(prices)
print(val)
