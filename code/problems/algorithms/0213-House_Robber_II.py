# -*- coding: utf-8 -*-
class Solution:
    def rob(self, nums) -> int:
        if len(nums) < 2:
            return self.safeRob(nums)
        rob_first=self.safeRob(nums[:-1])
        rob_second = self.safeRob(nums[1:])
        return max(rob_first, rob_second)

    def safeRob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[1]
        dp=[0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]

nums=[1,2,3,1]
r=Solution().rob(nums)
print(r)