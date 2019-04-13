# -*- coding: utf-8 -*-
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0
        minPrice=prices[0]
        maxProfit=0
        for i in range(1,len(prices)):
           e = prices[i]
           if e < minPrice:
               minPrice = e
           maxProfit = max(maxProfit, e - minPrice)
        return maxProfit

prices=[100,90,101]

r=Solution().maxProfit(prices)
print(r)
