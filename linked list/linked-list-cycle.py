'''
https://leetcode.com/problems/linked-list-cycle/
Notes:
fast and slow pointer approach will detect cycle
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False

        slow = head
        fast = head.next

        while fast:

            if slow == fast:
                return True
            
            slow = slow.next

            if fast.next:
                fast = fast.next.next
            else:
                fast = None

        return False