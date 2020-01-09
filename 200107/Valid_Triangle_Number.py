class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
#         any of two numbers are greater than the rest
#         duplicate case counts (2,2,3), (2,2,3)
        nums.sort()
        count = 0
        for i in range(len(nums) - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count


'''
if duplicate triplets don't count
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        count = 0
        for i in range(len(nums) - 1, 1, -1):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                continue
            l, r = 0, i - 1
            while l < r:
                if r < i - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue

                if nums[l] + nums[r] > nums[i]:
                    count += 1
                    r -= 1
                else:
                    l += 1
        return count

'''