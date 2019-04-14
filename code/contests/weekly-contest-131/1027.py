# -*- coding: utf-8 -*-
class Solution:
    def longestArithSeqLength(self, A) -> int:
        existingArithmeticArray = [A[:2]]
        for i in range(2,len(A)):
            e=A[i]
            existingArithmeticArray = self.getMaxSquence(existingArithmeticArray, e, len(A) - i - 1)
        return max(len(e) for e in existingArithmeticArray)


    def getMaxSquence(self, existingArithmeticArray, newElement, leftLen):

        newArray=[]
        currentMaxLength=2
        currentMaxGap=abs(existingArithmeticArray[0][1] - existingArithmeticArray[0][0])

        for i in range(len(existingArithmeticArray)-1, -1, -1):
            e = existingArithmeticArray[i]
            gap=e[-2] - e[-1]
            #非等差,选择jc
            if gap != e[-1] - newElement:
                # if abs(e[-1] - newElement) >= currentMaxGap:
                newArray.append([e[-1], newElement])
                # if abs(e[-2] - newElement) >= currentMaxGap:
                newArray.append([e[-2], newElement])
            else:
                e.append(newElement)
            # if len(e) + leftLen < currentMaxLength:
            if len(e)  < currentMaxLength:
                existingArithmeticArray.remove(e)
                continue
            currentMaxLength = max(len(e), currentMaxLength)
            currentMaxGap = max(abs(gap), currentMaxGap)

        existingArithmeticArray += newArray
        return existingArithmeticArray


A=[12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
r=Solution().longestArithSeqLength(A)
print(r)

# a=[1,2,3,4,5,6,7]
# for i in range(len(a)):
#     if i % 2 == 0:
#         a.remove(a[i])
