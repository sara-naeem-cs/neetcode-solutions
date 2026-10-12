class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        res = [] #Store resultant intervals
        
        #Sort intervals 
        intervals.sort(key=lambda i:i[0])

        #Add first interval to result
        res.append(intervals[0])


        for i in range(1, len(intervals)):
            if res[-1][1] > intervals[i][0]:
                #We have an overlapping interval
                res[-1][1] = min(res[-1][1], intervals[i][1])
            else:
                #No overlap so apped current interval to res
                res.append(intervals[i])
        
        return len(intervals)-len(res)
        