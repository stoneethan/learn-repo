def missingNumber(nums):
    res=len(nums)
    for i,num in enumerate(nums):
        res^=i^num
    return res


# 
# 这道题用异或法
# 就是通过同时异或下标和对应的数字的方法
# 相同异或为0
# 数字异或0为原数字
# 
