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

    return list(groups.value())

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
