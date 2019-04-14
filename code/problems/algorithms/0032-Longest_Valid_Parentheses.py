# -*- coding: utf-8 -*-
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        while len(s) > 0 and (s[:1] == ')' or s[-1:] == '('):
            s = s[1 if s[:1] == ')' else 0 : -1 if s[-1:] == '(' else len(s)]
        validString=""    #当前有效的字符串
        dp=[0] * (len(s) + 1 )
        judgeStack=[]
        for i in range(len(s)):
            e = s[i:i+1]
            dp[i + 1] = dp[i - 1]
            if e == '(':
                judgeStack.append('(')
            else:
                if len(judgeStack) > 0:
                    judgeStack.pop()
                    validString += "()"
                    dp[i + 1] = len(validString)
                else:
                    validString=""
        return max(dp)

param="()(()"
r=Solution().longestValidParentheses(param)
print(r)


