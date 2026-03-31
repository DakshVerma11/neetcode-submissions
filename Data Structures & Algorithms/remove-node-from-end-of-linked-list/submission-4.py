# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        for i in range(n):
            cur=cur.next
        target=head
        prev=None
        while cur:
            prev=target
            target=target.next
            cur=cur.next
        
        if not prev:
            return head.next
        
        
        prev.next=prev.next.next

        return head
        