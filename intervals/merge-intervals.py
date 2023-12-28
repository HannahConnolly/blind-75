""" 
https://leetcode.com/problems/merge-intervals/

  1  2   3  4
[[0, 2],[1, 3]]

"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals = sorted(intervals, key=lambda x: x[0])

        while i < len(intervals) - 1:
            # merge
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i] = [intervals[i][0], intervals[i + 1][1]]
                intervals.pop(i + 1)

            # no merge
            else:
                i += 1

        return intervals
