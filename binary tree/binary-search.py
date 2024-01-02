"""
https://leetcode.com/problems/binary-search/solutions/3363885/easy-solutions-in-java-python-and-c-look-at-once-with-exaplanation/
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] is target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
