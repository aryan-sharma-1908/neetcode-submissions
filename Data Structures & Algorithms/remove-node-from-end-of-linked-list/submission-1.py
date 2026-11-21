# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        length = 1
        while fast and fast.next:
            fast = fast.next.next
            length += 2
        
        if not fast:
            length -= 1
        
        nodeToRemove = length - n

        if nodeToRemove == 0:
            head = head.next
            return head
        temp = head

        while nodeToRemove != 1:
            temp = temp.next 
            nodeToRemove -= 1
        
        temp.next = temp.next.next

        return head