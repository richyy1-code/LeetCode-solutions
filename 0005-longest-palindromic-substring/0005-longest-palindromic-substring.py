class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
    
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1

        return res










        # if len(s) == 1:
        #     return s
        # res = ""
        # for i in range(len(s)):
        #     string = ""
        #     for j in range(i, len(s)):
        #         string += s[j]
        #         if string == string[::-1]:
        #             if len(string) > len(res):
        #                 res = string
        # return res

        


        
                    




