import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            temp_dist = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            heapq.heappush(heap, (temp_dist, point))

        res = []

        for i in range(k):
            smallest = heapq.heappop(heap)
            res.append(smallest[1])


        return res