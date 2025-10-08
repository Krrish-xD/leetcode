# Last updated: 08/10/2025, 14:07:51
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[j] = nums[i]
                prev = nums[i]
                j += 1
        return j