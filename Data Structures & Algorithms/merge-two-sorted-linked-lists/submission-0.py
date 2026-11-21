# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            connector = ListNode();
            head = ListNode();
            option1 = list1
            option2 = list2
            if (option1 and option2):
                if (option1.val < option2.val):
                    head = option1
                else:
                    head = option2
            if option1:
                option_bridge1 = option1.next
            if option2:
                option_bridge2 = option2.next
            while (option1 and option2):
                if (option1.val < option2.val):
                    connector.next = option1
                    connector = option1
                    option1 = option_bridge1
                    if (option_bridge1 == None):
                        connector.next = option2
                        break
                    option_bridge1 = option_bridge1.next
                else:
                    connector.next = option2
                    connector = option2
                    option2 = option_bridge2
                    if (option_bridge2 == None):
                        connector.next = option1
                        break
                    option_bridge2 = option_bridge2.next

            return head