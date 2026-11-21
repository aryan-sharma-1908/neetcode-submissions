# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry,itr1,itr2,dummy = 0, l1, l2, ListNode()
        nitr = dummy

        while itr1 and itr2:
            add = itr1.val + itr2.val + carry
            carry = 1 if add > 9 else 0
            nitr.next = ListNode((add) % 10)
            itr1 = itr1.next
            itr2 = itr2.next
            nitr = nitr.next

        

        while itr1:
            add = itr1.val + carry
            carry = 1 if add > 9 else 0
            nitr.next = ListNode((add) % 10)
            itr1 = itr1.next
            nitr = nitr.next

        while itr2:
            add = itr2.val + carry
            carry = 1 if add > 9 else 0
            nitr.next = ListNode((add) % 10)
            itr2 = itr2.next
            nitr = nitr.next

        if carry == 1:
            nitr.next = ListNode(1)
        return dummy.next
