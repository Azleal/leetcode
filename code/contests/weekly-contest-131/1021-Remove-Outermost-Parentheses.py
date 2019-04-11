# -*- coding: utf-8 -*-
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result=""
        start=0
        end=0
        currsor=[]
        if len(S) > 0:
            for i in range(len(S)):
                pointer=S[i:i+1]
                if len(currsor) == 0:
                    currsor.append(pointer)
                    start = i + 1
                else:
                    if '(' == pointer:
                        currsor.append(pointer)
                    else:
                        currsor.pop()
                    if len(currsor) == 0:
                        end = i
                        result += S[start:end]
        return result






solution = Solution();
t=solution.removeOuterParentheses("()()")
print(t)