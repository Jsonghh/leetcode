class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        ans, heights = 0, [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                       heights[j] = 0
                else:
                       heights[j] += 1
            ans = max(ans, self.helper(heights))

        return ans
                
            
    def helper(self, heights):
        heights = [0] + heights + [0]

        stack, ans = [], 0

        for idx, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                popidx = stack.pop()
                cur_area = heights[popidx] * (idx - stack[-1] - 1)
                ans = max(ans, cur_area)

            stack.append(idx)
            
        return ans