# Last updated: 07/10/2025, 01:12:38
class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        signf = False
        sign = 1

        for ch in s.strip():
            if ch.isdigit():
                res = res * 10 + int(ch)
                signf = True
            elif ch in ('-', '+') and not signf:
                sign = -1 if ch == '-' else 1
                signf = True
            else:
                break

        res *= sign
        return res if -2147483648 <= res <= 2147483647 else -2147483648 if res < 0 else 2147483647