# Last updated: 06/10/2025, 23:37:36
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))