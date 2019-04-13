# -*- coding: utf-8 -*-
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            定义dp[i]为爬到i阶楼梯的不重复爬法总数, 那么对于i >= 3的阶梯都有:
                1. 从i-2一下一步到第i阶,共有dp[i-2]种爬法
                2. 从i-2阶一下一步到第i阶,共有dp[i-2]种爬法
                3. 从i-1阶一下一步到第i阶,共有dp[i-1]种爬法
                4. 因为第1中爬法必然会经过第i-1阶, 因此爬法1和爬法3中有重叠的部分,也就是dp[i-2]种爬法
            总结以上: 对于i>=3, dp[i] = dp[i-2] * 2 + dp[i-1] - dp[i-2] = dp[i-2] + dp[i-1]
        '''
        dp=[0] * (n+2)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]




