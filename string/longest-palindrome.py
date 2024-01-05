'''
https://leetcode.com/problems/longest-palindrome/
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:

        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        
        pal_size = 0
        longest_odd = 0

        print(s_dict)

        for item in s_dict.items():

            if item[1] % 2 != 1:
                pal_size += item[1]
            elif item[1] > longest_odd:
                longest_odd = item[1]

        pal_size += longest_odd

        return pal_size