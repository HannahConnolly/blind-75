'''
https://leetcode.com/problems/climbing-stairs/

Notes:
    This is a fibbonacci sequence

    you can only traverse one or two steps at a time, therefore we know that every
    previous step determines the output of your new step, pictured below

    Step: 0 1 2 3 4 5
          8 5 3 2 1 1
          ^ amount of different ways a step can be taken up to step 5
          IE 1 from 4 (one step)
             2 from 3 (one twice or twice once)
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two # add two prev values and get new res
            two = temp
        
        return one
    
    def climbStairsBad(self, n: int) -> int:

        # reached the bottom
        if n is 0 or n is 1:
            return 1

        # traverse
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)
        