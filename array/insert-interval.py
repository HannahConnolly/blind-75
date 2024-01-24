class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        START = 0
        END = 1
        output = []

        for interval in intervals:
            # original is before new
            if interval[END] < newInterval[START]:
                output.append(interval)

            # original is after new
            elif interval[START] > newInterval[END]:
                output.append(newInterval)
                newInterval = interval

            # overlap
            elif (
                interval[END] >= newInterval[START]
                or interval[START] <= newInterval[END]
            ):
                newInterval[START] = min(interval[START], newInterval[START])
                newInterval[END] = max(interval[END], newInterval[END])

        output.append(newInterval)
        return output
