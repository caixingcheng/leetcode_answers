# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getLen(head):
            len=0
            while(head):
                len += 1
                head = head.next
            return len
        listLen = getLen(head)
        if n > listLen or n < 0:
            return None
        dummy = ListNode(0, head)
        h = dummy
        n = listLen - n + 1
        for i in range(n-1):
            h = h.next
        h.next = h.next.next
        return dummy.next

