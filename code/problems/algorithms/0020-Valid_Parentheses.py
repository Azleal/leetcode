# -*- coding: utf-8 -*-
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = ["()", "[]", "{}"]
        for e in list(s):
            if e in "([{":
                stack.append(e)
            else:
                if stack.pop() + e not in parentheses:
                    return False
        return True




