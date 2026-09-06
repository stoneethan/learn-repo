def findDisappearedNumbers(nums):
    for i in range(len(nums)): 
        index=abs(nums[i])-1
        if nums[index]>0:
            nums[index]=-nums[index]
    res=[]
    for i in len(nums):
        if nums[i]>0:
            res.append(i+1)
    return res

findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1])

# 这道题使用标记法
# 对于遍历的每个数，减一作为下标index
# 对nums[index]取负数处理
# 最后大于0的就是没有出现的
# 
