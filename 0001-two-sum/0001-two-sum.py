class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_dict:
                return [my_dict[diff], i]
            my_dict[nums[i]] = i
