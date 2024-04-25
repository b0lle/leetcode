import pytest

from leetcode.ex_11_container_with_most_water import Solution


class TestLongestPalindromicSubstring:
    @pytest.mark.parametrize("input, expected", [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1)])
    def test_cases(self, input: int, expected):
        result: int = Solution().maxArea(input)

        assert expected == result
