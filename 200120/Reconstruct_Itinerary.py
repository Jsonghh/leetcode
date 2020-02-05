from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        tickets.sort()
        lines = defaultdict(list)
        for dep, ari in tickets:
            lines[dep].append(ari)
        ans = []
        self.helper('JFK', lines, ans)
        return ans[::-1]
    
    
    def helper(self, dep, lines, ans):
        next_stops = lines[dep]
        while next_stops:
            self.helper(next_stops.pop(0), lines, ans)
        ans.append(dep)
        
        