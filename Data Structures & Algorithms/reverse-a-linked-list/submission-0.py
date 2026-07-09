# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            next=curr.next #next node ni save chestadhi
            curr.next=prev #flipping
            prev=curr #previous to one node
            curr= next #move to 1 step
        return prev    
        