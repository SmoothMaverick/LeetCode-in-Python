from typing import List


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head

        for i in range(index + 1):
            if curr == None:
                break

            if i == index:
                return curr.val

            curr = curr.next

        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        node = MyNode(val)
        node.next = self.head

        if self.head == None:
            self.tail = node

        self.head = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head == None:
            self.addAtHead(val)
            return

        node = MyNode(val)

        self.tail.next = node
        self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end
        of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:
            self.addAtHead(val)
            return

        curr = self.head
        prev = None

        for i in range(index + 1):
            if curr == None:
                if i == index:
                    self.addAtTail(val)
                    return
                else:
                    return

            if i == index:
                node = MyNode(val)
                node.next = curr
                prev.next = node
                return

            prev = curr
            curr = curr.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head == None:
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        prev = None

        for i in range(index + 1):
            if curr == None:
                return

            if i == index:
                if curr == self.tail:
                    self.tail = prev

                prev.next = curr.next
                return

            prev = curr
            curr = curr.next


class MyNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
