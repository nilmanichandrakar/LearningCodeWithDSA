# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        a1= head
        a2 = a3= head.next
        while(a2 and a2.next):
            a1.next = a2.next
            a1= a1.next
            a2.next= a1.next
            a2= a2.next
        a1.next= a3
        return head
