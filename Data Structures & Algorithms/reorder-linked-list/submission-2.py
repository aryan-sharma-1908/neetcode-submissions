# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head) -> None:
        if not head or not head.next:
            return

        length = 0
        ptr = head
        # calculate the length of the list
        while ptr:
            ptr = ptr.next
            length += 1

        mid = (length - 1) // 2 + 1
        ptr = head


        # move to the middle of the list
        for _ in range(mid - 1):
            ptr = ptr.next

        second = ptr.next
        ptr.next = None

        prev = None
        
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        p1 = head
        p2 = prev

        while p2:
            nxt1 = p1.next
            nxt2 = p2.next

            p1.next = p2
            p2.next = nxt1

            p1 = nxt1
            p2 = nxt2

