# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from day37 import ListNode

# 1 2 3 4
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        current = slow
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        max_sum = 0
        head1 = head
        head2 = prev
        while head2:
            max_sum = max(max_sum, head2.val + head1.val)
            head1 = head1.next
            head2 = head2.next
        return max_sum

