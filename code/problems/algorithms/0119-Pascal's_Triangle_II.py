# -*- coding: utf-8 -*-
class Solution:
    def getRow(self, rowIndex: int) :
        cheatSheet=[None] * 34
        cheatSheet[0] = 1
        for i in range(1, rowIndex + 1):
            cheatSheet[i] = cheatSheet[i - 1] * i

        sum=[]
        for i in range(1, rowIndex + 2):
            sum.append(int(cheatSheet[rowIndex] / (cheatSheet[i - 1] * cheatSheet[rowIndex + 1 - i])))
        return sum




rowIndex=4
sum = Solution().getRow(rowIndex)
print(sum)