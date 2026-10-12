import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        
        #Create a heap:
        heapq.heapify(stones)

        while len(stones) > 1:
            h1 = heapq.heappop(stones)*-1
            h2 = heapq.heappop(stones)*-1

            #If equal do nothing


            if h1 < h2:
                #Update amounts
                h2 = h2 - h1
                #Append new amounts to the heap
                heapq.heappush(stones, h2*-1)

            if h2 < h1:
                #Update amounts
                h1 = h1 - h2
                #Append new amounts to the heap
                heapq.heappush(stones, h1*-1)

        if stones:
            return heapq.heappop(stones)*-1
        else:
            return 0


