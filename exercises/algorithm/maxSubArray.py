def maxSubArray(num):
    dp=[0]*len(num)
    dp[0]=num[0]
    m=0
    for i in range(1,len(num)-1):
        dp[i]=max(num[i],dp[i-1]+num[i])
        m=max(m,dp[i])
    return m

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))