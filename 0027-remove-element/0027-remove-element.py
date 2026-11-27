class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0
        right = 0
        k = 0
        while right < len(nums):
            while left < len(nums) and nums[left] != val:
                left += 1
                right += 1
                k += 1
            if left != right and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
                left += 1
                k += 1
            else:
                right += 1
        return k

        




        