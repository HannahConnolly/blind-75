"""
https://leetcode.com/problems/valid-anagram/solutions/66499/python-solutions-sort-and-dictionary/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            s_dict[char] = s_dict.get(char, 0) - 1

        for key, value in s_dict.items():
            if value is not 0:
                return False

        return True
