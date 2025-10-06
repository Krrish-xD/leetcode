# Last updated: 07/10/2025, 01:12:39
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        res = 0
        while x:
            temp = x%10
            res = (res*10) +temp
            if not (-2147483648 <= res <= 2147483648 - 1):
                return 0
            x //= 10
           
        res *= sign
        return res if -2147483648 <= res <= 2147483648 - 1 else 0