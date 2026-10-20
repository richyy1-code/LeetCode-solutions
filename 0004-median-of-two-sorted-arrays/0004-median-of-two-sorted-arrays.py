class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 == 1:
            med = nums[(length//2)]
        
        else:
            a = nums[(length//2)-1]
            b = nums[(length//2)]
            med = (a+b)/2
        return med

        