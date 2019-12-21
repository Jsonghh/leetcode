class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        water = 0
        while left <= right:
            if l_max <= r_max:
                l_max = max(l_max, height[left])
                water += l_max - height[left]
                left += 1
            else:
                r_max = max(r_max, height[right])
                water += r_max - height[right]
                right -= 1
        return water
        
#         l_max = []
#         cur_max = -1
#         for v in height:
#             cur_max = max(v, cur_max)
#             l_max.append(cur_max)
#         r_max = []
#         cur_max = -1
#         for v in height[::-1]:
#             cur_max = max(v, cur_max)
#             r_max.append(cur_max)
#         r_max = r_max[::-1]
        
#         water  = 0
#         for i in range(len(height)):
#             water += min(l_max[i], r_max[i]) - height[i]
            
#         return water
                
        
        