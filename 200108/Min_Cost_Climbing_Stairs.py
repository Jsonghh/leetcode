
class Solution:
    """
    @param cost: an array
    @return: minimum cost to reach the top of the floor
    Status Conversion Function dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2])
    """

    def minCostClimbingStairs(self, cost):
        expense_2, expense_1, expense_0 = 0, 0, 0 
        for i in range(2, len(cost) + 1):
            expense_0 = min(expense_2 + cost[i-2], expense_1 + cost[i-1])
            expense_1, expense_2 = expense_0, expense_1
        return expense_0

        # if len(cost) < 2: return 0
        # if len(cost) == 2: return min(cost[0],cost[1])
        # dp = [0, 0]
        # for i in range(2, len(cost)+1):
        #     dp.append(min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]));
        # return dp[-1]



'''
Self-made Memorization Search
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         top: idx >= len(cost)
        memo = {}
        memo[0] = min(self.helper(cost, 0, memo), self.helper(cost, 1, memo))
        
        return memo[0]
    
    
    def helper(self, cost, cur_step, memo):
        if cur_step in memo:
            return memo[cur_step]
        if cur_step > len(cost) - 3:
            memo[cur_step] = cost[cur_step]
            return memo[cur_step]
        
        memo[cur_step] = cost[cur_step] + min(self.helper(cost, cur_step + 1, memo), self.helper(cost, cur_step + 2, memo))
        return memo[cur_step]
'''


	
