# -*- coding: utf-8 -*-
class Solution:
    def threeSum(self, nums):
        result = set()
        nums.sort()
        for i in range(len(nums)):
            e = nums[i]
            if e == 0 and i+2 < len(nums) and nums[i + 1] == nums[i + 2] and nums[i + 1] == 0:
                result.add([0,0,0])
                break
            elif e < 0:
                pass


        pass







nums = [-1, 0, 1, 2, -1, -4]
r=Solution().threeSum(nums)
print(r)