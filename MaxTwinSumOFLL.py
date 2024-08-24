# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sum = []
        while head:
            sum.append(head.val)
            head = head.next
        n = len(sum)
        res= max(sum[i] + sum[-(i + 1)] for i in range(n >> 1))
        return res
