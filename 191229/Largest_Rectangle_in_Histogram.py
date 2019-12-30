class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack, ans = [], 0
        for idx, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                poped_idx = stack.pop()
                cur_area = heights[poped_idx] * (idx - stack[-1] - 1)
                ans = max(ans, cur_area)
            stack.append(idx)
        return ans
                

