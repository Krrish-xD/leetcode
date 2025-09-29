# Last updated: 29/09/2025, 15:45:25
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letmap = {}
        for l in s:
            if l in letmap:
                letmap[l] += 1
            else:
                letmap[l] = 1
        for l in t:
            if l in letmap:
                letmap[l] -= 1
                if letmap[l] < 0:
                    return False
            else:
                return False
        for key, value in letmap.items():
            if value != 0:
                return False
        return True