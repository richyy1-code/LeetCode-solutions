class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        my_nums = set(nums)
        max_length = 0
        cur_length = 1

        for number in my_nums:
            if number-1 in my_nums:
                continue
            while number+1 in my_nums:
                cur_length += 1
                number += 1
            if cur_length > max_length:
                max_length = cur_length
            cur_length = 1
        return max_length
        