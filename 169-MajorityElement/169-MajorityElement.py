# Last updated: 05/10/2025, 17:16:39
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # res = None
        # curr = 0

        # for num in nums:
        #     if curr == 0:
        #         res = num
        #     curr += 1 if num == res else -1

        # return res

        nums.sort()
        n = len(nums)
        return nums[n//2]