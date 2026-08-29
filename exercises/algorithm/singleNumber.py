def singleNumber(nums):
    num_set = set()  # ✅ 正确：使用 set() 创建空集合，不要用 {}
    
    for i in range(len(nums)):
        if nums[i] in num_set:
            num_set.remove(nums[i])
        else:
            num_set.add(nums[i])  # ✅ 现在是 set 类型了，可以使用 add()
            
    return num_set.pop()

print(singleNumber([1, 2, 3, 3, 2]))  # 输出：1