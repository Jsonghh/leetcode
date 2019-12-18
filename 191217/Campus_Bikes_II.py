class Solution:
    def __init__(self):
        self.min_dist = float('inf')
        
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
#         fix workers, permutate bikes
        if not workers or not bikes:
            return 0
        
        bikes_to_assign_possi = self.get_possi_bikes(bikes, len(workers))
        
        for bikes_to_assign in bikes_to_assign_possi:
            bikes_permutation, visited = [], set()
            self.helper(bikes_to_assign, [], bikes_permutation, visited)
            for bikes_order in bikes_permutation:
                dist = 0
                for w, b in zip(workers, bikes_order):
                    dist += abs(w[0] - b[0]) + abs(w[1] - b[1])
                self.min_dist = min(self.min_dist, dist)
        return self.min_dist
    
    
    def helper(self, bikes, cur_list, per, visited):
        if len(cur_list) == len(bikes):
            per.append(cur_list[:])
            return
        for i in range(len(bikes)):
            if i not in visited:
                visited.add(i)
                cur_list.append(bikes[i])
                self.helper(bikes, cur_list, per, visited)
                visited.remove(i)
                cur_list.pop()
        return
    
    def get_possi_bikes(self, bikes, n):
        ans = []
        self._helper(bikes, 0, [], ans, n)
        return ans
    
    def _helper(self, bikes, start_idx, cur_list, ans, n):
        if len(cur_list) == n:
            ans.append(cur_list[:])
            return
        
        for i in range(start_idx, len(bikes)):
            cur_list.append(bikes[i])
            self._helper(bikes, i + 1, cur_list, ans, n)
            cur_list.pop()
        return
        
        
        