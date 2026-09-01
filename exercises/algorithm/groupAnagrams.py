# from collections import defaultdict

# def groupAnagrams(strs):
#     groups=defaultdict(list)
#     for s in strs:
#         key="".join(sorted(s))
#         groups[key].append(s)
#     return list(groups.values())

# groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


# 上面是排序法
# 思路是排序之后的串作为key，直接在值上加入对应的字符串
# 最后把结果字典转化为list
# default(list)是指字典不存在key默认生成一个list
#字典添加也需要注意：groups[key].append(values)

from collections import defaultdict

def groupAnagrams(strs):
    groups=defaultdict(list)

    for s in strs:
        count=[0]*26
        for c in s:
            index=ord(c)-ord('a')
            count[index]+=1
        groups[tuple(count)].append(s)

    return list(groups.values())

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

# 上面的方法是计数法
# 原则就是记录每一个串的频次表转化为元组（a:1,b:2)作为字典的key
# 然后加入对应字串就好
# 注意values()
# 注意频次表  count[ord(c)-ord('a)]+=1
# ord是把字符转化为对应数字
