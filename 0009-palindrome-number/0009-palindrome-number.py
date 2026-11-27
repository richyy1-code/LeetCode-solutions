class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left = 0
        right = len(s) - 1
        while right > left:
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1
        return True
        

        # if x < 0:
        #     return False
        # div = 1
        # while x >= div:
        #     div *= 10
        # div/=10
        # while x != 0:
        #     if x%10 ==  x//div:
        #         x%=div
        #         x//=10
        #         div/=100
        #     else:
        #         return False
        # return True
        

