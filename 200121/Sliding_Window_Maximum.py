class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque, ans = [], []
        for i in range(len(nums)):
            while deque and nums[i] >= nums[deque[-1]]:
                deque.pop()
            
            deque.append(i)
            
            if i + 1 >= k:
                ans.append(nums[deque[0]])
            if deque[0] == i + 1 - k:
                deque.pop(0)
        return ans