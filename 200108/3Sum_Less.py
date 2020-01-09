class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        if not nums:
            return 0
        cnt = 0
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum < target:
                    cnt += r - l
                    l += 1
                else:
                    r -= 1
        return cnt
            
        