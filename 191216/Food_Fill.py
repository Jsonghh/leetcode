class Solution:
    def __init__(self):      
        self.visited = set()
        # self.cur_color = None
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or not image[0]:
            return 
        cur_color = image[sr][sc]
        self.cur_color = cur_color
        self.helper(image, sr, sc, newColor)
        return image
    
    
    def helper(self, image, sr, sc, newColor):
        image[sr][sc] = newColor
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for dr, dc in moves:
            nr, nc = sr + dr, sc + dc
            if (nr, nc) not in self.visited and 0 <= nr < len(image) and 0 <= nc < len(image[0]):
                if image[nr][nc] != self.cur_color:
                    continue
                self.visited.add((nr, nc))
                self.floodFill(image, nr, nc, newColor)
        