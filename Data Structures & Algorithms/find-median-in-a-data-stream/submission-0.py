class MedianFinder:

    def __init__(self):
        #create two heaps
        self.max_heap=[]
        self.min_heap=[]

    def addNum(self, num: int) -> None:
        #over here we add to the heap (two heaps?)
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -1*num)

    def findMedian(self) -> float:
        return (self.min_heap[0] + (-1*self.max_heap[0]))/2
        
        