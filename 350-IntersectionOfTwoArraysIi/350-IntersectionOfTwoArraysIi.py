# Last updated: 29/09/2025, 20:11:10
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        res = []
        for key, value in cnt1.items():
            if key in cnt2:
                res += [key]*(min(value, cnt2[key]))
        return res