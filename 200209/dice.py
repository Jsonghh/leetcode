class Solution:
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)
        max_count = -1
        for i in range(len(points) - 1):
            max_count = max(self.max_points_on_line_i(i, points), max_count)
        return max_count
    
    
    def max_points_on_line_i(self, i, points):
        lines= {}
        count, points_ver, dup = 1, 1, 0
        
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2 and y1 == y2:
                dup += 1
            elif x1 == x2:
                points_ver += 1
            else:
                slope = (y1 - y2) / (x1 - x2)
                lines[slope] = lines.get(slope, 1) + 1
                count = max(lines[slope], count)
                
        return max(count, points_ver) + dup
            
print(Solution().maxPoints([[0,0],[94911151,94911150],[94911152,94911151]]))