# Last updated: 05/10/2025, 17:16:45
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashm = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            hashm[key].append(s)

        return list(hashm.values())