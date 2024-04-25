from typing import List
from leetcode.ex_4_median_of_two_sorted_arrays import Solution
import pytest


class TestMedianOfTwoSortedArrays:
    @pytest.mark.parametrize("num_1, num_2, expected", [([1, 3], [2], 2.00000), ([1, 2], [3, 4], 2.50000)])
    def test_case_1(self, num_1: List[int], num_2: List[int], expected: float):
        result: float = Solution().findMedianSortedArrays(nums1=num_1, nums2=num_2)

        assert result == expected
