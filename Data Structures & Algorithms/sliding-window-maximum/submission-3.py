import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #To create max heap multiply values by -1
        for i in range(len(nums)):
            nums[i] = nums[i]*-1
        
        #Create heap (with first k elements)
        heap = []
        heapq.heapify(heap)

        for i in range(k):
            if i<k:
                #For the first window we push to the heap
                heapq.heappush(heap, (nums[i], i))
            
            
        res = []
        res.append(heap[0][0]*-1)
        windowStart = 0
        windowEnd = k

        #Now slide the window until windowEnd == len(nums)
        #Each time take the max value and add it to our res
        #If max is out of range then keep popping until we get a value that is in window range

        while windowEnd != len(nums):
            heapq.heappush(heap, (nums[windowEnd], windowEnd))
            maxValue, maxIndex = heap[0]
            windowStart += 1


            #Pop out outdated max values from our heap
            while maxIndex < windowStart:
                #Keep popping values
                maxValue, maxIndex = heapq.heappop(heap)

            maxValue, maxIndex = heap[0]

            res.append(-1*maxValue)
            windowEnd +=1


        return res

        

        