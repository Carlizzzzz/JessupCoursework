def get_max_profit(stock_prices):
    flag = 0
    for i in range(0,len(stock_prices)):
        for j in range(i+1,len(stock_prices)):
            if stock_prices[j]-stock_prices[i]> flag:
                flag = stock_prices[j]-stock_prices[i]
    return flag

stock_prices = [10, 7, 5, 8, 11, 9]

print(get_max_profit(stock_prices))