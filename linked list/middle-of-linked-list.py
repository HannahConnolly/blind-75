'''
https://leetcode.com/problems/middle-of-the-linked-list/submissions/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        if not head.next:
            return head

        slow = head
        fast = head.next

        while fast:
            if not fast.next:
                return slow.next
            
            fast = fast.next.next
            slow = slow.next

        return slow