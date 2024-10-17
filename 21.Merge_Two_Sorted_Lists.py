# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2
        dummy = ListNode(None)
        dummyHead = dummy

        while curr1 and curr2:
            if curr1.val >= curr2.val:
                dummy.next = curr2
                dummy = dummy.next
                curr2 = curr2.next
            else:
                dummy.next = curr1
                dummy = dummy.next
                curr1 = curr1.next
        
        if curr1: dummy.next = curr1
        if curr2: dummy.next = curr2

        return dummyHead.next
solution = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merged = solution.mergeTwoLists(list1, list2)

curr = merged
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next