def maxProfit(prices):
    if not prices:
        return 0
    n=len(prices)
    dp=[0]*n
    min_num=prices[0]

    for i in range(1,n,1):
        min_num=min(min_num,dp[i])
        dp[i]=max(dp[i-1],prices[i]-min_num)

    return dp[n-1]

print(maxProfit([7,1,5,6,4]))

