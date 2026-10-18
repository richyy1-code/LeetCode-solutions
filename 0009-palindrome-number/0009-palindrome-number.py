class Solution:
    def isPalindrome(self, x: int) -> bool:
        old_s = str(x)
        pos = -1
        steps = len(old_s)//2
        for i in range(steps):
            if old_s[i] == old_s[pos]:
                pos -= 1
            else:
                return False
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
        

