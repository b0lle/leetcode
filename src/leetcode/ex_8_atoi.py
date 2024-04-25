class Solution:
    def myAtoi(self, s: str) -> int:
        x = s.strip()
        if len(x) == 0:
            return 0
        sign = x[0] in ["-", "+"]
        x = x[1:] if sign else x
        if len(x) == 0:
            return 0
        if ord(x[0]) not in range(48,58):
            return 0
        for i in range(len(x)):
            if ord(x[i]) not in range(48,58):
                break
        else:
            i += 1
        x = int(s[0] + x[:i]) if sign else int(x[:i])
        return min(max(x, -2**31), 2**31 - 1)



# print(Solution().myAtoi("42")) # 42
# print(Solution().myAtoi("words and 987")) # 42
print(Solution().myAtoi("    -42")) # 42
