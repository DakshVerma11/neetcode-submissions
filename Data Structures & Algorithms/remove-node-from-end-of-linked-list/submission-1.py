# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        cur=head
        while cur:
            count+=1
            cur=cur.next
            
        
        pos=count-n
        cur=head
        
        if pos==0:
            if count==1:
                return None
            return head.next
        
        while pos>1:
            cur=cur.next
            pos-=1
        
        if cur.next:
            cur.next=cur.next.next
        else:
            cur.next=None
        return head