"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        count = 0 
        max_count = 0

        i = 0
        j = 0 

        while i != len(start) and j!= len(end):
            if start[i] < end[j]:
                #New meeting started
                count = count + 1
                i = i + 1
            elif start[i] > end[j]:
                count = count - 1
                j = j + 1
            else:
                #Both same value, meeting started and ended
                j = j + 1
                count = count - 1
                i = i + 1
                count = count + 1
            max_count = max(count, max_count)

        return max_count
        