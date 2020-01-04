class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid
            else:
                r = mid
        if nums[r] > nums[l]:
            return r
        else:
            return l