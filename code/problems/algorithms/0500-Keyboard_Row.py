# -*- coding: utf-8 -*-
class Solution:
    def findWords(self, words):
        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        results = []
        for word in words:
            loweredWord = word.lower()
            hitRowIndex = None
            for i in range(len(loweredWord)):
                e = loweredWord[i:i+1]
                currentHitRowIndex=0
                if e in rows[0]:
                    currentHitRowIndex = 0
                elif e in rows[1]:
                    currentHitRowIndex = 1
                else:
                    currentHitRowIndex = 2

                if hitRowIndex is None:
                    hitRowIndex = currentHitRowIndex
                elif hitRowIndex != currentHitRowIndex:
                    hitRowIndex = None
                    break

            if hitRowIndex is not None:
                results.append(word)
        return results


param=["Hello", "Alaska", "Dad", "Peace"]
r=Solution().findWords(param)
print(r)
