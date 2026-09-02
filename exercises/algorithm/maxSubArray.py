def maxSubArray(num):
    dp=[0]*len(num)
    dp[0]=num[0]
    m=0
    for i in range(1,len(num)-1):
        dp[i]=max(num[i],dp[i-1]+num[i])
        m=max(m,dp[i])
    return m

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


# 这是一个动态规划
# 动态规划步骤
# 1.建立dp,初始化
# 2.确立dp[0]等基础已知条件
# 3.建立前后关系
