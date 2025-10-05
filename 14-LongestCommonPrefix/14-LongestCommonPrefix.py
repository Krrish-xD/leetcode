# Last updated: 05/10/2025, 17:16:46
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        for chars in zip(*strs):
            if (len(set(chars))-1):
                break
            res += (chars[0])
            
        return "".join(res)