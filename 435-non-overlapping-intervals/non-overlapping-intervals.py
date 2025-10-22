class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        non_overlapping = intervals[0][1]
        count=0
        for i in range(1,len(intervals)):
            if intervals[i][0] < non_overlapping:
                count+=1
                non_overlapping = min(intervals[i][1],non_overlapping)
            else:
                non_overlapping = intervals[i][1]


        return count