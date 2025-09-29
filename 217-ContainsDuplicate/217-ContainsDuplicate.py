# Last updated: 29/09/2025, 15:45:27
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not(len(nums) == len(set(nums)))