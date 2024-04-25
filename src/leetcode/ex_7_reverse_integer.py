class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        rev = int(s[::-1])
        if rev < -2**31 -1 or rev > 2**31:
            return 0
        return rev

print(Solution().reverse(123)) # 321
