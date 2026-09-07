def lengthOfLongestSubstring(s):
    char_index={}
    maxlen=0
    slow=0
    for fast in range(len(s)):
        char=s[fast]
        if char in char_index and char_index[char]>=slow:
            slow=char_index[char]+1
        char_index[char]=fast
        length=fast-slow+1
        maxlen=max(maxlen,length)
    return maxlen

print(lengthOfLongestSubstring("abcabcbb"))

# 这道题用快慢指针+滑动窗口
# 快慢指针维护一个窗口，快指针右移
# 出现重复就移动慢指针缩小窗口
# 记录更新窗口的最大长度
# 
# 
