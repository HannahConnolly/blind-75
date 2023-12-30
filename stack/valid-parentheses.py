'''
https://leetcode.com/problems/valid-parentheses/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        # define bracket stacks
        brackets = []

        # helper function to remove from stack
        def valid_removal(type: str) -> bool:

            if len(brackets) == 0:
                return False
            if brackets.pop() is not type:
                return False

            return True

        for char in s:

            match char:

                # Append open brackets
                case '(':
                    brackets.append(char)
                case '[':
                    brackets.append('[')
                case '{':
                    brackets.append('{')

                # Remove corresponding bracket if is closed
                case ')':
                    if(not valid_removal('(')):
                        return False
                case ']':
                    if(not valid_removal('[')):
                        return False
                case '}':
                    if(not valid_removal('{')):
                        return False
                
        
        return not brackets 

       