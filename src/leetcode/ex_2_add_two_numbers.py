# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from ast import List
from typing import Optional
from xmlrpc.client import Boolean



class Solution:
    @staticmethod
    def add_list_nodes(l1, l2, add_one: bool):
        if l1 is None and l2 is None:
            if not add_one:
                raise RuntimeError("shouldnt be called")
            return ListNode(val=1)
        elif l1 and l2:
            real_val = l1.val +  l2.val
            l1_next = l1.next
            l2_next = l2.next
        elif l1 and l2 is None:
            l1_next = l1.next
            l2_next = None
            real_val = l1.val
        elif l1 is None and l2:
            l1_next = None
            l2_next = l2.next
            real_val = l2.val
        if add_one:
            real_val += 1
        val = real_val
        if real_val > 9:
            val -= 10
        if l1_next is not None or l2_next is not None:
            return ListNode(val=val, next=Solution.add_list_nodes(l1_next, l2_next, add_one=real_val>9))
        if real_val > 9:
            return ListNode(val=val, next=Solution.add_list_nodes(l1=None, l2=None, add_one=True))
        return ListNode(val=val)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res = self.add_list_nodes(l1=l1, l2=l2, add_one=False)
        return res

    @staticmethod
    def list_node_to_list(l1):
        _l1 = []
        while True:
            _l1.append(l1.val)
            if l1.next is None:
                break
            l1 = l1.next
        return _l1

    @staticmethod
    def create_list_node(res):
        next = None
        if len(res) >= 2:
            next = Solution.create_list_node(res[1:])
        return ListNode(val=res[0], next=next)


class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        _l1 = self.list_node_to_list(l1=l1)
        _l2 = self.list_node_to_list(l1=l2)

        calc = lambda l: int(("").join(map(str, l[-1::-1])))
        num_1 = calc(_l1)
        num_2 = calc(_l2)
        sum_int = num_1 + num_2
        res = [int(c) for c in str(sum_int)][-1::-1]
        res_2 = self.create_list_node(res)
        return res_2

    @staticmethod
    def list_node_to_list(l1):
        _l1 = []
        while True:
            _l1.append(l1.val)
            if l1.next is None:
                break
            l1 = l1.next
        return _l1

    @staticmethod
    def create_list_node(res):
        next = None
        if len(res) >= 2:
            next = Solution1.create_list_node(res[1:])
        return ListNode(val=res[0], next=next)

