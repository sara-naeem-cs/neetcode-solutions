import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(i, j):
            xi, yi = points[i]
            xj, yj = points[j]
            return abs(xi - xj) + abs(yi - yj)

        n = len(points)
        found = set()
        cost = 0
        minHeap = [(0, 0)]  # (distance, index) — start at index 0

        while len(found) < n:
            dist, node = heapq.heappop(minHeap)

            if node in found:
                continue

            found.add(node)
            cost += dist

            for neighbor in range(n):
                if neighbor not in found:
                    d = manhattan(node, neighbor)
                    heapq.heappush(minHeap, (d, neighbor))

        return cost