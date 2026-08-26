
def longestPrefix(strs:list[str]):
    if not strs:
        return ""

    for j in range(len(strs[0])):
        char=strs[0][j]
        for i in range(1,len(strs)):
            if j==len(strs[i]) or strs[i][j]!=char:
                return strs[0][:j]
    return strs[0]

