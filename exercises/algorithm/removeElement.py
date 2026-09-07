def removeElement(nums, val):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast]!=val:
            nums[slow]=nums[fast]
            slow+=1

    return slow


print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))

# 这道题记住关键逻辑
# 删除数组中的元素的逻辑：
# 快指针走向非目标值数字，慢指针接受
# 这样慢指针指向的都是非目标值数字
