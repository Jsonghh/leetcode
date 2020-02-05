import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = (x ** 2 + y ** 2) ** 0.5
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > K:
                heapq.heappop(heap)
                
        ans = []
        while heap:
            dist_, x, y = heapq.heappop(heap)
            ans.append([x, y])
            
        return ans
            
            
        
