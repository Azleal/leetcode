# -*- coding: utf-8 -*-
class Solution:
    def thirdMax(self, nums):
        result = [float('-inf')] * 3
        for e in nums:
            if e not in result:
                if e > result[0]:
                    result = [e, result[0],result[1]]
                elif e > result[1]:
                    result = [result[0], e, result[1]]
                elif e > result[2]:
                    result = [result[0],result[1],e]
        return max(nums) if float('-inf') in result else result[2]




# param=[1,2,2]
param=[1,2,2,5,3,5]
r=Solution().thirdMax(param)
print(r)


