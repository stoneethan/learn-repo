def firstUniqChar(s):

    dict={}
    for c in s:
        if c in dict:
            dict[c]+=1
        else:
            dict[c]=1

    for i in range(0,len(s)):
        if dict[s[i]]==1:
            return i

    return -1

firstUniqChar("ajdhhais")

# 这个题用的是频次表解决
# 注意语法先判断字典里面是否有初始值，否则报Keyerror
# dict[c]+=1
# 
