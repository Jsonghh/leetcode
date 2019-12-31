class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            sum3 = self.threeSum(nums[i + 1:], target - nums[i])
            if sum3:
                for sub_ans in sum3:
                    ans.append([nums[i]] + sub_ans)
        return ans
    
    
    def threeSum(self, nums, target):
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                if nums[l] + nums[r] + nums[i] == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif nums[l] + nums[r] + nums[i] > target:
                    r -= 1
                else:
                    l += 1
        return ans
            
        