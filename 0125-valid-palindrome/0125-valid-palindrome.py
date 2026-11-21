class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s:
            if char.isalpha():
                res += char.lower()
            elif char.isdigit():
                res += char
        return True if res == res[::-1] else False

        