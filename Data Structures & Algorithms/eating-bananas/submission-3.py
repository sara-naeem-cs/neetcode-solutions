import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = 0

        for pile in piles:
            max_val = max(pile, max_val)

        l = 1
        r = max_val 
        ret = max_val

        while l<=r:
            mid = (l+r)//2

            #Now we test out this k
            total_hours = 0
            for pile in piles:
                total_hours = total_hours + math.ceil(pile/mid)
            
            if total_hours <= h:
                #Our current rate too small, update left
                r = mid - 1
                ret = min(ret, mid)
            else:
                l = mid + 1
        
        return ret
                





                

        
