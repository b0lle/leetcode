from decimal import Decimal
import itertools
from math import floor
from numbers import Real
from operator import length_hint
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)

        len_nums: int = len(nums1)
        if len_nums == 1:
            return nums1[0]
        elif len_nums % 2 == 0:
            middle_low: int = floor(len_nums / 2) - 1
            middle_high: int = floor(len_nums / 2)
            return (nums1[middle_low] + nums1[middle_high]) / 2
        return nums1[floor(len_nums / 2)]
