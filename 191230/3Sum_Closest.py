class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum == target:
                    return target
                
                if abs(cur_sum - target) < abs(ans - target):
                    ans = cur_sum
                
                if cur_sum > target:
                    r -= 1
                else:
                    l += 1
        return ans