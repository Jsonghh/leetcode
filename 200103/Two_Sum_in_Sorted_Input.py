class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # all_idx = {}
        # for idx, num in enumerate(numbers):
        #     other = target - num
        #     if other in all_idx:
        #         return [all_idx[other], idx + 1]
        #     all_idx[num] = idx + 1
        # return [-1, -1]
        
        
#       as the list is already sorted, we don't need to use extra space
        l, r = 0, len(numbers) - 1
        while l < r:
            tmp_sum = numbers[l] + numbers[r]
            if tmp_sum == target:
                return [l + 1, r + 1]
            elif tmp_sum < target:
                l += 1
            else:
                r -= 1
        return [-1, -1]
        