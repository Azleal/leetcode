# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums , target) :
        nums=[[nums[i], i] for i in range(len(nums))]
        nums.sort()
        frontPointer = 0
        reerPointer = len(nums) - 1
        a,b = None, None
        while frontPointer < reerPointer:
            if nums[frontPointer][0] + nums [reerPointer][0] == target :
                a,b = nums[frontPointer][1], nums [reerPointer][1]
                break;
            elif nums[frontPointer][0] + nums [reerPointer][0] < target :
                frontPointer += 1
            elif nums[frontPointer][0] + nums [reerPointer][0] > target :
                reerPointer -= 1
        return [a,b]



# nums = [2, 11, 15,7]
# target = 9
# Solution().twoSum(nums, target)


nums = [3,3]
target = 6
r = Solution().twoSum(nums, target)
print(r)


