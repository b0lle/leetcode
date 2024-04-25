# Definition for singly-linked list.
import cProfile
from re import sub
from sqlite3 import SQLITE_LIMIT_VARIABLE_NUMBER
import stat
from typing import Dict, Optional, Set, Tuple, List
from xmlrpc.client import Boolean
import cProfile, pstats, io
from pstats import SortKey


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charIndex = [-1] * 128
        left = 0

        for right in range(n):
            if charIndex[ord(s[right])] >= left:
                left = charIndex[ord(s[right])] + 1
            charIndex[ord(s[right])] = right
            maxLength = max(maxLength, right - left + 1)

        return maxLength
