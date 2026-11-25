class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        # left = 0
        # right = 0
        # while right < len(nums):
        #     if nums[right] == 0:
        #         right += 1
        #     elif nums[right] != 0 and left != right:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         right += 1
        #         left += 1
        #     else:
        #         right += 1
        #         left += 1
            

        