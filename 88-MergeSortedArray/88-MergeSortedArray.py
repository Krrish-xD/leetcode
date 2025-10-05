# Last updated: 05/10/2025, 17:16:40
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
            return
        if n == 0:
            # nums1 = nums1[:m]
            return
        
        l1 = l2 = 0
        nums = [0] * (m+n)

        for i in range(m+n):
            if l1 == m:
                nums[i:] = nums2[l2:]
                break
            if l2 == n:
                nums[i:] = nums1[l1:m]
                break

            if nums1[l1] < nums2[l2]:
                nums[i] = nums1[l1]
                l1 += 1
            else:
                nums[i] = nums2[l2]
                l2 += 1

        nums1[:] = nums

        return
        
        
