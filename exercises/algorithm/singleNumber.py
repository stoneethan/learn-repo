def singleNumber(nums:list[int])->int:
    set={}
    for i in range(-1,len(nums)-1,1):
        if nums[i] in set:
            set.remove(nums[i])
        else:
            set.add(nums[i])

    return next(iter(set))

singleNumber([1,2,3,3,2])
