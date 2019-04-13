# -*- coding: utf-8 -*-
class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


nums=[-2,1,-3,4,-1,2,1,-5,4]
r=Solution().maxSubArray(nums)
print(r)
