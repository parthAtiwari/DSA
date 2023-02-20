# gain max profit by buying and selling a stock one time
def buy_sell_stock_once(prices):
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        profit = price-min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)
    return max_profit
