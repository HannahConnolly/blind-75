'''
https://leetcode.com/problems/add-binary/solutions/1680441/easy-python-solution/

Notes:
This code is a simple implementation of converting binary numbers to integers, 
adding them, and then converting the sum back to binary.
The conversion of binary to integer is done using the int() method with a base of 2, 
which means that it will treat the string as a binary number and return the equivalent integer. 
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        return bin(x + y)[2:]