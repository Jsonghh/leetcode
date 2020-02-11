class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        people_amount = len(costs)
        n = people_amount // 2
        cost = 0
        
#         sort by costs[0] - costs[1]
        costs.sort(key=lambda x : x[0] - x[1])
    
        for i in range(n):
            cost += costs[i][0] + costs[i + n][1]
            
        return cost
        