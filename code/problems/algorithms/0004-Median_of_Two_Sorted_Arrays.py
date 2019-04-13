# -*- coding: utf-8 -*-
class Solution:
    def findMedianSortedArrays(self, nums1 , nums2) -> float:

        if ((nums1[0] > nums2[0] and nums1[-1] > nums2[-1]) or (nums1[0] <= nums2[0] or nums1[-1] >= nums2[-1])):
            nums1,nums2 = nums2, nums1

        print(nums1, nums2)



num2=[1,3]
num1=[2]
Solution().findMedianSortedArrays(num1, num2)