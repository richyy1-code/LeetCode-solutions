class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1]
        cur_product = 1
        for i in range(1, len(nums)):
            cur_product *= nums[i-1]
            answer.append(cur_product)
        cur_product = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                cur_product = 1
            else:
                cur_product *= nums[i+1]
            answer[i] *= cur_product
        return answer
        