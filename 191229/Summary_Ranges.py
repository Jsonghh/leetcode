class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        start, end = nums[0], nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i] + 1:
                end = nums[i]
                if start != end:
                    ans.append(str(start) + '->' + str(end))
                else:
                    ans.append(str(start))
                start = nums[i + 1]
                
        end = nums[-1]
        if start != end:
            ans.append(str(start) + '->' + str(end))
        else:
            ans.append(str(start))
        return ans

            
        
            
        