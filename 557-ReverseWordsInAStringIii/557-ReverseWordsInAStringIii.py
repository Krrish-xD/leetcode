# Last updated: 06/10/2025, 23:37:32
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(w[::-1] for w in s.split()))
