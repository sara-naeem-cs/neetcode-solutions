import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_val = max(piles)
        
        l = 0
        r = max_val
        

        while l<r:
            mid = (l+r)//2

            #check if at the current mid value we can eat all piles in h 
            temp_hours = 0

            for i in range(len(piles)):
                temp_hours = temp_hours + math.ceil(piles[i]/mid)

            if temp_hours > h:
                #we need a larger k (eating too slow)
                l = mid + 1
            else:
                r = mid
        
        return l

                

        
