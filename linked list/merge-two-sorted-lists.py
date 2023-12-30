"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        # Set head of new list
        out = None
        if list1.val < list2.val:
            out = list1
            list1 = list1.next
        else:
            out = list2
            list2 = list2.next

        head = out

        # add nodes to list of nodes
        while list1 and list2:
            if list1.val < list2.val:
                out.next = list1
                list1 = list1.next

            else:
                out.next = list2
                list2 = list2.next

            out = out.next

        while list1:
            out.next = list1
            list1 = list1.next
            out = out.next

        while list2:
            out.next = list2
            list2 = list2.next
            out = out.next

        return head
