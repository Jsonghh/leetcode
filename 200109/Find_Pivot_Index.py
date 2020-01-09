class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)
        
        for idx, presum in enumerate(presums):
            if idx == 0:
                continue
            to_left, to_right = presums[idx - 1], presums[-1] - presum
            if to_left == to_right:
                return idx - 1
        return -1
        