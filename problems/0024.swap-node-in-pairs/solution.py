from typing import List

"""
1. Recursively visit each node to the end of the linked-list.
2. Swap the pointers
    a. next node points to head node
    b. head node points to previous node
3. Return the next node to be used as previous node in the next stack
4. Finally return the new head
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.swap(head)

    def swap(self, head: ListNode):
        if head == None or head.next == None:
            return head

        prev_node = self.swap(head.next.next)
        next_node = head.next

        head.next.next = head
        head.next = prev_node

        return next_node