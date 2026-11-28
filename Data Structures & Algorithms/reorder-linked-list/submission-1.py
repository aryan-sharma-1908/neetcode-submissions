# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head) -> None:
        length = 0
        ptr = head
        # calculate the length of the list
        while ptr:
            ptr = ptr.next
            length += 1
        # calculate the middle of the list
        mid = (length - 1) // 2 + 1
        ptr = head
        # move to the middle of the list
        while mid > 1:
            ptr = ptr.next
            mid -= 1
        p = ptr
        ptr = ptr.next
        p.next = None
        temp = None
        if ptr:
            ptrn = ptr.next
        
        while ptr:
            ptr.next = temp
            temp = ptr
            ptr = ptrn
            if ptrn:
                ptrn = ptrn.next
        p2 = temp
        p1 = head
        if p2:
            p2n = p2.next
        while p2:
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = p2n 
            if p2n:
                p2n = p2n.next
