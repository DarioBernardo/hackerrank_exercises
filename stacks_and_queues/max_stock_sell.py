

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


def max_profit_2(price_list: list):
    #  check for len array

    index = 2
    buy_stack = [0]
    sell_stack = [1]
    profit_stack = [price_list[1] - price_list[0]]

    while index < len(price_list):
        daily_price = price_list[index]

        # in case we have a new min in the stack
        if len(buy_stack) != len(sell_stack):
            current_profit = daily_price - price_list[buy_stack[-1]]
            while len(profit_stack) > 0 and current_profit > profit_stack[-1]:
                profit_stack.pop(-1)
                sell_stack.pop(-1)
                buy_stack.pop(-2)

            profit_stack.append(current_profit)
            sell_stack.append(index)

        if len(sell_stack) > 0 and daily_price > price_list[sell_stack[-1]]:

            while len(sell_stack) > 0 and daily_price > price_list[sell_stack[-1]]:
                sell_stack.pop(-1)
                profit_stack.pop(-1)

            sell_stack.append(index)
            current_profit = daily_price - price_list[buy_stack[-1]]
            profit_stack.append(current_profit)

        else:
            if len(sell_stack) > 0 and daily_price < price_list[buy_stack[-1]]:
                if len(buy_stack) != len(sell_stack):
                    buy_stack.pop(-1)
                else:
                    buy_stack.append(index)

        index += 1

    # flush the array
    print(buy_stack)
    print(sell_stack)
    print(profit_stack)


max_profit_2(prices)
