'''
https://leetcode.com/problems/majority-element/solutions/
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return nums[0]

        num_dict = {}
        max_element = nums[0]

        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
            if num_dict[num] > num_dict[max_element]:
                max_element = num

        print(num_dict)
        return max_element
        