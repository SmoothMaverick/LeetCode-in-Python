import unittest
from solution import MyLinkedList


class TestDesignLinkedList(unittest.TestCase):
    def runTest(self):
        obj = MyLinkedList([])
        obj.addAtHead(1)
        obj.addAtTail(3)
        obj.addAtIndex(1, 2)
        self.assertEqual(obj.get(1), 2)
        obj.deleteAtIndex(1)
        self.assertEqual(obj.get(1), 3)


if __name__ == "main":
    unittest.main()
