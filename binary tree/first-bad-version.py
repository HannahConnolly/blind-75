'''
https://leetcode.com/problems/first-bad-version/submissions/

Notes:
must use parens before division ;_;
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # binary search to find first bad version
        start = 0
        end = n
        mid = n // 2
        
        while end > start:
            print('- - -')
            print(start, mid, end)
            print(isBadVersion(mid))
            
            # test if mid is bad (true) end becomes mid and test again
            if isBadVersion(mid):
                end = mid
                mid = (end + start) // 2

            # mid is good (false) start becomes mid and test again
            else:
                if (end - mid) <= 1:
                    return end

                start = mid
                mid = (end + start) // 2