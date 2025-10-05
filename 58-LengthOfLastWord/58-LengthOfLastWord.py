# Last updated: 05/10/2025, 17:21:14
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        letF = False
        curr = 0
        for c in s[::-1]:
            if c != ' ':
                letF = True
                curr += 1
            elif letF:
                return curr
        return curr