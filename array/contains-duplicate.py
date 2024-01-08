'''
https://leetcode.com/problems/contains-duplicate/submissions/

Notes:
One liner instantiates the set with the array as an arg
return len(set(nums)) != len(nums)
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)

        return False
