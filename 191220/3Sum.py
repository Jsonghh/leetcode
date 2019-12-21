class Solution1:
    '''
    Use 2Sum template, looking for the other part
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            rest = self.helper(nums[i + 1:], target)
            for r in rest:
                ans.append([nums[i]] + r)
        return ans
        
    def helper(self, nums, target):
        d, matched = set(), set()
        rest = []
        for i in range(len(nums)):
            other = target - nums[i]
            if i > 0 and nums[i - 1] == nums[i] and other in matched:
                continue
            if other in d :
                rest.append([other, nums[i]])
                matched.add(other)
            d.add(nums[i])
        return rest
            

class Solution2:
    '''
    Do not use extra space
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            target = -nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if start > i + 1 and nums[start] == nums[start - 1]:
                    start += 1
                    continue
                cur_sum = nums[start] + nums[end]
                if cur_sum == target:
                    ans.append([nums[i], nums[start], nums[end]])
                    start += 1
                if cur_sum < target:
                    start += 1
                if cur_sum > target:
                    end -= 1
        return ans
                    
            