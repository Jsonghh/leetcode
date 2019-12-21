class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left_b, right_b, up_b, down_b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        ans = []
        direction = 0
        cnt = len(matrix) * len(matrix[0])
        while cnt:
            cur_dir = direction % 4
            if cur_dir == 0:
                for i in range(left_b, right_b + 1):
                    ans.append(matrix[up_b][i]) 
                    cnt -= 1
                up_b += 1
            if cur_dir == 1:
                for i in range(up_b, down_b + 1):
                    ans.append(matrix[i][right_b])
                    cnt -= 1
                right_b -= 1
            if cur_dir == 2:
                for i in range(right_b, left_b - 1, -1):
                    ans.append(matrix[down_b][i])
                    cnt -= 1
                down_b -= 1
            if cur_dir == 3:
                for i in range(down_b, up_b - 1, -1):
                    ans.append(matrix[i][left_b])
                    cnt -= 1
                left_b += 1
                    
            direction += 1
        return ans
      
        
        