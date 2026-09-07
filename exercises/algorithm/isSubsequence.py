def isSubsequence(s,t):
    index=0

    for fast in range(len(t)):
        if index<len(s) and s[index]==t[fast]:
            index+=1

    return index==len(s)
# 这道题我们使用双指针法
# 一个指针定位s里的字符，另一个遍历t中的
# 匹配到一个就慢指针向前走
# 为了防止越界，我们只需要加上一个判断条件就好
# 最后返回值我们用是否慢指针走到头来处理
# 
