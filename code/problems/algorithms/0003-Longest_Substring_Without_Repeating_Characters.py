# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = []
        currentSubstr=[]
        start = 0
        end = 1
        while end <= len(s) + 1:
            # print("longest", longest, "currentSubstr", currentSubstr)
            c = s[end -1: end]
            if c not in currentSubstr:
                currentSubstr = list(s[start:end])
            else:
                start = s.find(c, start, end) + 1
                longest = currentSubstr if len(longest) < len(currentSubstr) else longest
                currentSubstr = list(s[start:end])
            end += 1
        longest = currentSubstr if len(longest) < len(currentSubstr) else longest
        return len(longest)



# param="bbbbb"

# param="abcabcbb"

param=" "

r=Solution().lengthOfLongestSubstring(param)
print(r)