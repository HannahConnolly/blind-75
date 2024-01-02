"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 99999999
        diff = 0

        for price in prices:
            if min > price:
                print("min found")
                min = price

            if (price - min) > diff:
                diff = price - min
                print("min")

        return diff
