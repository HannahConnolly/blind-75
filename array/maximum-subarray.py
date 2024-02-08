"""
https://leetcode.com/problems/maximum-subarray/

Notes:
Don't overthink this one, the max sum will slowly grow as long as
it doesn't reduce below 0 (intuitive)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum = 0
        max_sum = 0

        for num in nums:

            sum += num
            max_sum = max(sum, max_sum)

            sum = sum if sum > 0 else 0

        return max_sum
