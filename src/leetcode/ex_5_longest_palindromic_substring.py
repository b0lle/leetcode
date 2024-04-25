import itertools


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest: str = s[0]
        for i in range(len(s)):
            for n in range(i + 1, len(s) + 1):
                x = s[i:n]
                if x == x[::-1]:
                    if len(x) > len(longest):
                        longest = x
        return longest
