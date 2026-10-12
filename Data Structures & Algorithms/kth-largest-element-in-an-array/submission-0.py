import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)):
            #Negate all values
            nums[i] = -1*nums[i]
        
        #Create our heap
        heapq.heapify(nums)

        for i in range(k):
            smallest = heapq.heappop(nums)
        
        return smallest*-1
