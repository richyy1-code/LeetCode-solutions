class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True




       
       
       
       
       
       
       
       
       
        # res = ""
        # for char in s:
        #     if char.isalpha():
        #         res += char.lower()
        #     elif char.isdigit():
        #         res += char
        # return True if res == res[::-1] else False

        