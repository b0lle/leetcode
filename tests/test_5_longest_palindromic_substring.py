import pytest
from leetcode.ex_5_longest_palindromic_substring import Solution


class TestLongestPalindromicSubstring:
    @pytest.mark.parametrize("input, expected", [("babad", "bab"), ("cbbd", "bb"), ("bb", "bb")])
    def test_cases(self, input: str, expected: str):
        result: str = Solution().longestPalindrome(s=input)

        assert expected == result
