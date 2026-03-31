# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        for i in lists:
            cur=i
            while cur:
                res.append(cur.val)
                cur=cur=cur.next
        if not res:
            return None
        res.sort()

        
        head= ListNode()
        cur=head
        for val in res:
            cur.next=ListNode(val)
            cur=cur.next

        return head.next
