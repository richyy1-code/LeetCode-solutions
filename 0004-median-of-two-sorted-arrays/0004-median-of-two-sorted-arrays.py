class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 == 1:
            return nums[(length//2)]
        a = nums[(length//2)-1]
        b = nums[(length//2)]
        return (a+b)/2


        