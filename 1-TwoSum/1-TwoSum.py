# Last updated: 29/09/2025, 15:45:26
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i, num in enumerate(nums):
            if target-num in hashm:
                return [hashm[target-num], i]
            hashm[num] = i
        return []