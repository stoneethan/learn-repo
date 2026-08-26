
def longestPrefix(strs:list[str]):
    tar=0
    for i in range(len(strs)-2):
        for j in range(len(strs[1])-1):
            if strs[i][j]==strs[i+1][j]:
                tar+=1
            else:
                break
    return tar

longestPrefix(["flower","flow","flight"])
