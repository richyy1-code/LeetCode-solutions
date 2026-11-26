class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        right = 0
        k = 1

        while right < len(nums):
            if nums[right] != nums[left]:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
                k += 1

            else:
                right += 1

        return k



        

