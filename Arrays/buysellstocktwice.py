# Write a program that computes the maximum profit that can be made by buying and selling a shareat most twice.
# The second buy must be made on another date after the first sale.

#  Solution:
# The idea is to first iterate left to right (L->R) & to store the max profit in an array at the index where you can
# think of selling the stock ( at each index you can sell but you can not have max profit at each index, right?).
# so store the maximum previous profit you can get till now.

# In the second iteration iterate in reverse direction (R->L)  from n-1 to 1 ( not till 0 because at 0 index you can
# only buy!)
# maintain a max_price variable (because we are iteration in reverse ) similar to first iteration in which we store
# min_price because we were keeping track of minimum price at which we can buy the stock.
# to avoid using another array for reverse we can add the previous max profit of forward iteration( because  max profit
# in the array will be already in ascending order) by adding element at (i-1)th index.

def buy_sell_stock_at_most_twice(prices):
    min_price=float('inf')
    max_profit=0
    day1 = [0 for i in range(len(prices))]
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i]-min_price)
        day1[i] = max_profit

    high_of_day = float('-inf')
    for i in range(len(prices)-1,0,-1):
        high_of_day = max(high_of_day, prices[i])
        max_profit = max(max_profit, high_of_day-prices[i]+day1[i-1])
    return max_profit










