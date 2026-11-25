class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True
        
        

        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)

        # if len(s) != len(t):
        #     return False
        # count = [0] * 26
        # for a, b in zip(s, t):
        #     count[ord(a) - ord('a')] += 1
        #     count[ord(b) - ord('a')] -= 1
        # return all(c == 0 for c in count)
        
        