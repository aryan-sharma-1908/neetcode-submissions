# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
            
        prevprev = None
        prev = head
        next = head.next
        

        while next:
            prev.next = prevprev
            prevprev = prev
            prev = next
            next = next.next

        prev.next = prevprev

        return prev