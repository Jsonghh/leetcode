import heapq
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        heapqs = {}     
        test = []
        for sid, score in items:
            if sid == 2:
                test.append((sid,score))
            if sid not in heapqs:
                heapqs[sid] = []
            hq = heapqs[sid]
            if len(hq) < 5:
                heapq.heappush(hq, score)
            elif score > hq[0]:
                heapq.heappop(hq)
                heapq.heappush(hq, score)
        ans = []
        for sid, hq in heapqs.items():
            ans.append([sid, sum(hq) // len(hq)])
        return ans
            
            
        
        