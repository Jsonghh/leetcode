class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        if not heights:
            return heights
        if K < 0 or K >= len(heights):
            return heights
        
        for i in range(V):
            self.helper(heights, K)
        return heights
        
        
    def helper(self, heights, k):
        while self.move_left(heights, k):
            k -= 1

        while self.move_right(heights, k):
            k += 1

        heights[k] += 1
        return

    
    def move_left(self, heights, k):
        for i in range(k - 1, -1, -1):
            if heights[i] > heights[k]:
                return False
            if heights[i] < heights[k]:
                return True
        return False
        
    
    def move_right(self, heights, k):
        for i in range(k + 1, len(heights)):
            if heights[i] > heights[k]:
                return False
            if heights[i] < heights[k]:
                return True
        return False        