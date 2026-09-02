def merge(nums1,m,nums2,n):
    p1,p2,i=m-1,n-1,m+n-1
    while p2>=0:
        if p1>=0 and nums1[p1]>nums2[p2]:
            nums1[i]=nums1[p1]
            p1-=1
        else:
            nums1[i]=nums2[p2]
            p2-=1
        i-=1
    return nums1

print(merge(nums1=[1], m=1, nums2=[], n=0))


# 这个题思路是三指针
# 两个指针用来定位有元素数组，一个用来定位返回数组的位置
# 此外因为nums1结尾是一些0，所以倒着遍历
# 
