# Last updated: 07/10/2025, 01:12:25
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l<r:

            if s[l] != s[r]:
                r1, r2 = s[l+1:r+1], s[l:r]
                return r1 == r1[::-1] or r2 == r2[::-1]

            l += 1
            r -= 1

        return True