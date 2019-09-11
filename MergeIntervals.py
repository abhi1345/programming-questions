class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: x[0])
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                newInterval = [intervals[i][0], 
                               max(intervals[i+1][1], intervals[i][1])]
                intervals[i] = newInterval
                intervals.pop(i+1)
            else:
                i += 1
        return intervals
