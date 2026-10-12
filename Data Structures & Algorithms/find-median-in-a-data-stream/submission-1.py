import heapq


class MedianFinder:
    # median is middle number or mid1 + mid2 / 2
    def __init__(self):
        # create two heaps
        self.max_heap = []  # small heap
        self.min_heap = []  # Big heap

    def addNum(self, num: int) -> None:
        # Add number to max heap (small heap)
        heapq.heappush(self.max_heap, -1 * num)

        # Max Heap < Min Heap:
        if self.min_heap and self.max_heap and self.max_heap[0] * -1 > self.min_heap[0]:
            # pop from max and add to min
            smallest_val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, smallest_val * -1)

        # Check Sizes:
        if len(self.max_heap) > len(self.min_heap)+1:
            # pop from max and add to min
            smallest_val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, smallest_val * -1)

        if self.min_heap and self.max_heap and len(self.min_heap) > len(self.max_heap):
            # pop from max and add to min
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val * -1)

    def findMedian(self) -> float:
        # If we have odd length we get the most middle number:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0] * -1

        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        return (-self.max_heap[0] + self.min_heap[0]) / 2
