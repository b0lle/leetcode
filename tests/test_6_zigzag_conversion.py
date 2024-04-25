import pytest
from leetcode.ex_6_zigzag_conversion import Solution


class TestLongestPalindromicSubstring:
    @pytest.mark.parametrize(
        "s, num_rows, expected", [("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"), ("PAYPALISHIRING", 4, "PINALSIGYAHRPI")]
    )
    def test_cases(self, s: str, num_rows: int, expected):
        result: str = Solution().convert(s=s, numRows=num_rows)

        assert expected == result
