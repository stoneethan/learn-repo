from collections import Counter
def isIsomorphic(s,t):
    if len(s)!=len(t):
        return False

    map_s_t,map_t_s={},{}

    for a,b in zip(s,t):
        if a in map_s_t and map_s_t[a]!=b:
            return False
        if b in map_t_s and map_t_s[b]!=a:
            return False
        map_s_t[a]=b
        map_t_s[b]=a

    return True


print(isIsomorphic(s = "egg", t = "add"))

# 同构字符串做法
# 先比较两串是否等长，不等长就不行
# 然后循环遍历比较每个串对应字符是否有对应关系
# 如果都有，代表True
# 对应关系就用两个map
# a,b in zip(s,t)可以将两个对应位的字符打包比较
# 先检查现两个字符是否和原状态冲突，然后记录新状态

