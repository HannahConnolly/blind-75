import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for point in points:
            distance = self.findDistance(point)

            if len(heap) == k:
                heap.heappushpop(heap, (dist, point))

            else:
                heap.heappush(heap, (dist, point))

        return [point for (point) in heap]

    def findDistance(self, point: List[int]) -> float:
        return sqrt(abs(point[0] * point[0]) + abs(point[1] * point[1]))
