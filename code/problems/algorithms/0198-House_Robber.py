# -*- coding: utf-8 -*-
class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0:
            return 0
        '''
        H[i]表示第i个房子里的钱数
        f[i]表示: 从第1个到第i个房子, 藏钱最多的且不触发报警的抢法能抢的最多钱数.
        那么f[i] = max(f[i-2] + H[i], f[i-1]),即要么抢了前一个房子(i-1),要么隔着抢了钱一个房子(i-2)和这个房子H[i]
        '''
        f = [0] * (len(nums) + 1)
        f[1] = nums[0]
        for i in range(2, len(nums) + 1):
            f[i] = max(f[i-2] + nums[i - 1], f[i-1])
        print(f)
        return f[-1]

nums=[2,7,9,3,1]
Solution().rob(nums)