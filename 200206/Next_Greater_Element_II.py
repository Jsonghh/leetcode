class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, d = [], {}
        
        circular = nums + nums[:-1]
        
        for i in range(len(circular)):
            while stack and circular[stack[-1]] < circular[i]:
                smaller_idx = stack.pop()
                d[smaller_idx] = i
                
            stack.append(i)
            
        ans = []
        for idx in range(len(nums)):
            if idx in d:
                ans.append(circular[d[idx]])
            else:
                ans.append(-1)
                
        return ans
            
        