"""
https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        front_ptr = 0
        back_ptr = len(s) - 1

        deq = Deque()
        for char in s:
            if char.isalpha() or char.isdigit():
                deq.append(char.lower())

        while len(deq) > 1:
            left = deq.popleft()
            right = deq.pop()

            if left != right:
                print(left, right)
                return False

        return True
