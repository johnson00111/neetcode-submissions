"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # If there is conflict means that we need to add 1 meeting room
        intervals.sort(key=lambda x:x.start)
        ans = 1
        hp = []
        heapq.heappush(hp, intervals[0].end)
        
        for i in range(1, len(intervals)):
            while hp and intervals[i].start >= hp[0]:
                heapq.heappop(hp)
            heapq.heappush(hp, intervals[i].end)
            ans = max(ans, len(hp))

        return ans
        
        # [(0,10),(1,3),(2,6),(5,8),(7,12),(11,15),(13,18),(16,20),(19,25),(24,30)]
        # hp = [25, 30] ans = 3
        # (19, 25)
