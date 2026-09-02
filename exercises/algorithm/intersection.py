def intersection(nums1,nums2):
    return list(set(nums1)&set(nums2))


res=intersection(nums1 = [1,2,2,1], nums2 = [2,2])
print(res)

# 这道题看重复元素
# 可以将两个转化为集合，然后与运算，算出都有的东西
# 最后转化为list
