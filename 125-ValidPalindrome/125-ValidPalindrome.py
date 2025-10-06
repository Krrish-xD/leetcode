# Last updated: 07/10/2025, 01:12:30
class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = re.sub(r"[^A-Za-z0-9]", "", s).lower()
        return formatted == formatted[::-1]