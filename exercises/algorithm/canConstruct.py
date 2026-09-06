def canConstruct(ransomNote,magazine):
    count={}
    for char in magazine:
        count[char]=count.get(char,0)+1

    for char in ransomNote:
        if count[char]==0 or char not in count:
            return False
        count[char]-=1

    return True

print(canConstruct(ransomNote = "aa", magazine = "aab"))

# 使用哈希表法来做这道题
# 先记录杂志中的字串资源，然后消耗
# 哲学思想是先获取资源然后消耗
# 先判断，然后更新状态
