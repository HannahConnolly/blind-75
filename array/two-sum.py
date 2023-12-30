"""
https://leetcode.com/problems/two-sum

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for idx, num in enumerate(nums):
            if target - num in my_dict:
                return [my_dict[target - num], idx]

            else:
                my_dict[num] = idx

        return []
