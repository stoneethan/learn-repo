def reverseString(s):
    p1,p2=0,len(s)-1
    while p2>=p1:
        s[p1],s[p2]=s[p2],s[p1]
        p1+=1
        p2-=1

    return s

print(reverseString(s = ["h","e","l","l","o"]))


# 同样是双指针
# 注意py交换的写法s[1],s[2]=s[2],s[1]
# 
# 
