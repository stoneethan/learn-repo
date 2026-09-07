def removeDuplicates(nums):
    if not nums:
        return 0
    slow=0
    for fast in range(1,len(nums)):
        if nums[fast]!=nums[slow]:
            slow+=1
            nums[slow]=nums[fast]
    return slow+1

# 这道题使用双指针
# 快慢指针，快指针遍历数组
# 慢指针定位须改变的位置
# 
