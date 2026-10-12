class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        #Sort intervals by beginning number
        intervals.sort(key=lambda i : i[0])

        res.append(intervals[0])
        i = 1

        while i < len(intervals):
            #Intervals overlap so merge
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])

            #Intervals don't overlap so append new interval
            else:
                res.append(intervals[i])
            

            i = i + 1
        
        return res
        