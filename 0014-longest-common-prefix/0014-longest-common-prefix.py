class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        '''output = ""
        i = 0
        x = 1
        while i < len(strs[0]) and x == 1:
            cur_let = strs[0][i]
            for word in strs:
                if i < len(word) and word[i] == cur_let:
                    x = 1
                else:
                    x = 0
            if x == 1:
                output += cur_let
                i += 1

        return output'''

        output = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return output
            output += strs[0][i]
        return output