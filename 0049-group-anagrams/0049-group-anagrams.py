class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = {}

        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char)-97] += 1
            str_key = tuple(freq)
            if str_key in seen:
                seen[str_key].append(word)
                continue
            seen[str_key] = [word]
        return list(seen.values())
        