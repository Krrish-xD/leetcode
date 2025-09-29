# Last updated: 29/09/2025, 22:31:38
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for key, value in cnt.items():
            if value == 1:
                return s.index(key)
        return -1