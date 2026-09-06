def majorityElement(nums):
    candidate=None
    count=0
    for num in nums:
        if count==0:
            candidate=num
        count+=(1 if candidate==num else -1)
    return candidate

print(majorityElement([1,2,3,3,2,2,2]))


# 这道题使用摩尔投票法
# 维护一个数，记录最大的数，遇到相同数count+=1，其余减一
# 如果count==0,那么当前数被推选为最大数
# 维护一个默认为空的数：candidate=None
# 表达式count+=(1 if num==条件 else -1)
#             