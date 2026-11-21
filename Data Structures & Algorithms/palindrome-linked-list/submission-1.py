# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        x = slow
        
        stack = deque()

        while slow:
            stack.append(slow.val)
            slow = slow.next

        fast = head

        while fast != x:
            if(fast.val != stack.pop()):
                return False
            fast = fast.next

        return True
        