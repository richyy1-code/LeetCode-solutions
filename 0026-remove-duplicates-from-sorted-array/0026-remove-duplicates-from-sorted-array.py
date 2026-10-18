class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        e_list = []
        pos = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] not in e_list:
                nums[pos] = nums[i]
                e_list.append(nums[i])
                pos+=1
        return pos
        

