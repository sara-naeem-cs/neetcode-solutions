"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        #Sort meetings by start time
        intervals.sort(key=lambda i:i.start)

        curr = intervals[0]

        #Iterate through intervals, 
        for i in range(1, len(intervals)):
            if intervals[i].start < curr.end:
                return False
            else:
                curr = intervals[i]

        return True