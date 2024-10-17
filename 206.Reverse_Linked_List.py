# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None: return None

        curr = head
        dummy = None
        n = curr.next

        while curr.next:
            curr.next = dummy
            dummy = curr
            curr = n
            n = n.next
        curr.next = dummy
        return curr

solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
reversed = solution.reverseList(head)

curr = reversed
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next