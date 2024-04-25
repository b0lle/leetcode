from operator import ne
from leetcode.ex_2_add_two_numbers import ListNode, Solution1, Solution


class TestAddTwoNumbers:
    def test_case_1(self):
        l1 = Solution1.create_list_node([2, 4, 3])
        l2 = Solution1.create_list_node([5, 6, 4])

        result = Solution().addTwoNumbers(l1=l1, l2=l2)
        listed_result = Solution1.list_node_to_list(result)

        assert listed_result == [7, 0, 8]

    def test_case_2(self):
        l1 = ListNode(val=0)
        l2 = ListNode(val=0)

        result = Solution().addTwoNumbers(l1=l1, l2=l2)
        listed_result = Solution1.list_node_to_list(result)

        assert listed_result == [0]

    def test_case_3(self):
        l1 = Solution1.create_list_node([9, 9, 9, 9, 9, 9, 9])
        l2 = Solution1.create_list_node([9, 9, 9, 9])

        result = Solution().addTwoNumbers(l1=l1, l2=l2)
        listed_result = Solution1.list_node_to_list(result)

        assert listed_result == [8, 9, 9, 9, 0, 0, 0, 1]
