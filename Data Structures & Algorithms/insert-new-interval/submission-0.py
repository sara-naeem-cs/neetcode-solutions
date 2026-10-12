class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [] 

        for i in range(len(intervals)):
            #If new interval end is < current interval start
            #Interval being inserted already passed so append
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:] #slice current result with rest of the list

            #If new interval start is greater than current interval end:
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) #append current interval
            #Else we have overlapping intervals and need to merge them
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        res.append(newInterval)  #If new interval is at the veryy end  
        return res