"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        last_end = -1

        for interval in intervals:
            start, end = interval.start, interval.end

            if start >= last_end:
                last_end = end
            else:
                return False
        
        return True