class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = {}

        for word in strs:
            str_key = tuple(sorted(word))
            if str_key in seen:
                seen[str_key].append(word)
                continue
            seen[str_key] = [word]
        return list(seen.values())

        