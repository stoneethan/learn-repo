from collections import Counter

def intersect(nums1,nums2):
    if len(nums1)>len(nums2):
        return intersect(nums2,nums1)
    count=Counter(nums1)
    res=[]
    for num in nums1:
        if num in count:
            count.get(num,0)>0
            res.append(num)
            count[num]-=1
    return res

print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))

# 这道题的解法是频次表法
# 将短长度的变成频次字典
# 在长长度的数组里遍历，遇到对应的数，呢么就频次减一
# Counter(nums1)代表创建一个nums1的频次表
# count.get(num,0)>0是一种获取次数并且能够防止key报错的安全写法
# def intersect(nums1,nums2):
#     if len(nums1)>len(nums2):
#         return intersect(nums2,nums1)
# 是一种把长度较小的数组放在前面的递归写法


