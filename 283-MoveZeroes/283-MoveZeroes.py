# Last updated: 08/10/2025, 14:07:41
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        
        for n in nums:
            if n:
                nums[i] = n
                i += 1
        
        l = len(nums)
        while i < l:
            nums[i] = 0
            i += 1