import cProfile
import io
from operator import ne
from pstats import SortKey
import pstats
from leetcode.ex_3_longest_substring_without_repeating_characters import Solution

pr = cProfile.Profile()


class TestLongestSubstringWithoutRepeatingCharacters:
    def test_case_1(self):
        pr.enable()
        result = Solution().lengthOfLongestSubstring("abcabcbb")
        assert result == 3
        pr.disable()
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

    def test_case_2(self):
        result = Solution().lengthOfLongestSubstring("bbbbb")
        assert result == 1

    def test_case_3(self):
        result = Solution().lengthOfLongestSubstring("pwwkew")
        assert result == 3

    def test_case_4(self):
        result = Solution().lengthOfLongestSubstring("")
        assert result == 0

    def test_case_5(self):
        result = Solution().lengthOfLongestSubstring(" ")
        assert result == 1
