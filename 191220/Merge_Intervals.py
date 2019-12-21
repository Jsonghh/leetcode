class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        ans = [intervals[0]]
        for start, end in intervals[1:]:
            if ans[-1][1] >= start:
                new_end = max(end, ans[-1][1])
                ans[-1][1] = new_end
            else:
                ans.append([start, end])
        return ans