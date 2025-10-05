# Last updated: 05/10/2025, 17:16:44
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = 0

        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            if res < curr:
                res = curr

        return res