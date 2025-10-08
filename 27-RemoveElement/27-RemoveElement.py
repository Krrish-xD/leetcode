# Last updated: 08/10/2025, 14:07:49
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        
        for n in nums:
            if n != val:
                nums[j] = n
                j += 1

        return j