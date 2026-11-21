class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0
        new_s = ""
        strings_list = []
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in new_s:
                    new_s += s[j]
                else:
                    strings_list.append(len(new_s))
                    new_s = ""
                    break         
        return max(strings_list)
