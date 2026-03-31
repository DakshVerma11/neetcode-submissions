# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            
            
        '''
        prev,mid,end=None,head,head

        while end and end.next:
            prev=mid
            mid=mid.next
            end=end.next.next


        if prev:
            prev.next=None
        prev = None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt


        
        cur = head
        mid = prev

        while cur and mid:
            nxt1 = cur.next
            nxt2 = mid.next

            cur.next = mid
            if not nxt1:
                break
            
            mid.next = nxt1

            cur = nxt1
            mid = nxt2

        return None
        '''