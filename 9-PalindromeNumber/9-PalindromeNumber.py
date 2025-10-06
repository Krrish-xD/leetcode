# Last updated: 07/10/2025, 01:12:36
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        return x1 == x1[::-1]