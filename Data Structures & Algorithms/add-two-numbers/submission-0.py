# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=0
        cur=l1
        base=1
        while cur:
            num1+=cur.val*base
            cur=cur.next
            base*=10
        
        
        num2=0
        cur=l2
        base=1
        while cur:
            num2+=cur.val*base
            cur=cur.next
            base*=10


        sumnum=num1+num2
        
        head=ListNode(sumnum%10)
        sumnum//=10
        cur=head
        while sumnum:
            cur.next=ListNode(sumnum%10)
            sumnum//=10
            cur=cur.next
        return head
        