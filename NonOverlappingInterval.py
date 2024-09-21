class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans, t = 0, intervals[0][1]
        for start, end in intervals[1:]:
            if start >= t:
                t = end
            else:
                ans += 1
        return ans
