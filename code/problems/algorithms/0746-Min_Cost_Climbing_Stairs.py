# -*- coding: utf-8 -*-
class Solution:
    '''
    cost[i]表示第i阶的cost
    dp[i]表示到i阶时的总cost, dp[i] = min(dp[i-2] + cost[i], dp[i-1] + cost[i])
    '''
    def minCostClimbingStairs(self, cost) -> int:
        cost.append(0)
        dp = [float('inf')] * (len(cost) + 1)
        dp[1] = cost[0]
        dp[2] = cost[1]
        for i in range(3, len(cost) + 1):
            e = cost[i - 1]
            dp[i] = min(dp[i-2] + e, dp[i-1] + e)
        return dp[-1] if len(cost) > 3 else min(dp)


cost = [1, 100]
r=Solution().minCostClimbingStairs(cost)
print(r)


