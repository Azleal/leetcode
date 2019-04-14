# -*- coding: utf-8 -*-
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[:1] == '0':
            return 0
        dp = [None] * len(s)
        dpd = [0] * len(s)  # 最后两位连续的数字的个数
        dps = [0] * len(s)  # 最后1位连续的数字的个数
        dps[0] = 1
        dp[0] = 1
        for i in range(1, len(s)):
            dps[i] = dp[i - 1] if s[i:i + 1] != '0' else 0
            dpd[i] = dps[i - 1] * 1 if int(s[i - 1:i + 1]) <= 26 else 0
            dp[i] = dpd[i] + dps[i]
            if s[i:i + 1] == '0' and int(s[i - 1:i + 1]) > 20:
                return 0
        return dp[-1]

param="32312003"
r=Solution().numDecodings(param)
print(r)