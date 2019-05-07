class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Iterative:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        rev_head = None
        curr_next = None

        while curr != None:
            curr_next = curr.next
            curr.next = rev_head
            rev_head = curr
            curr = curr_next

        return rev_head


class Recursive:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        rev_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return rev_head
