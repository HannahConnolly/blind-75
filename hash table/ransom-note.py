'''
https://leetcode.com/problems/ransom-note/submissions/
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # store number values in magazine dictionary
        magazine_dict = {}
        for char in magazine:
            magazine_dict[char] = magazine_dict.get(char, 0) + 1

        # destruct dictionary with chars in ransom note
        for char in ransomNote:
            val = magazine_dict.get(char, -1) - 1
            print(char, val)
            if val < 0:
                return False
            else:
                magazine_dict[char] = val
            
        return True