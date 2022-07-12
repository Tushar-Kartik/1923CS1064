def stock_buy_sell(prices):
    l=0
    r=1
    maxp=0
    while r<len(prices):
        #profit ?
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            maxp = max(profit,maxp)
        else:
            l=r
        r+=1

    return maxp

prices=[7,1,5,3,6,4]
print(stock_buy_sell(prices))

