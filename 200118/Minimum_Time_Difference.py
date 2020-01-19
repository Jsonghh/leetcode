class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if not timePoints:
            return 0
        RANGE = 24 * 60
        minutes = [0] * RANGE
        max_time = -1
        if len(timePoints) > RANGE:
            return 0
        
        for time in timePoints:
            time_minute = self.convert_minute(time)
            minutes[time_minute] += 1
            
            if minutes[time_minute] > 1:
                return 0
            
            max_time =  time_minute if time_minute > max_time else max_time
            
        min_diff, prev = RANGE, None
        for time_minute in range(RANGE):
            if minutes[time_minute] == 0:
                continue
            if not prev:
                diff = time_minute + RANGE - max_time
            else:
                diff = time_minute - prev
            min_diff = diff if diff < min_diff else min_diff
            prev = time_minute
            
        return min_diff
    
    def convert_minute(self, s):
        hour, minute = s.split(':')
        return int(hour) * 60 + int(minute)
            
            
        