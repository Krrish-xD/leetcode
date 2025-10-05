# Last updated: 05/10/2025, 17:16:42
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1
        print(length)
        while length >= 0:
            if digits[length] == 9:
                digits[length] = 0
                length -= 1
            else:
                digits[length] += 1
                return digits
        return [1] + digits