import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
                
        ans = heapq.heappop(heap)
            
        return ans
            
        
        
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    # Time Complexity: O(N)
    def kthLargestElement(self, k, nums):
        # write your code here
        if not nums:
            return -1
            
        self.qsort(nums, 0, len(nums) - 1, len(nums) - k)
        return nums[len(nums) - k]
        
        
    def qsort(self, nums, start, end, k):
        if start == end:
            return
        left, right = start, end
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
                
        if k <= right:
            self.qsort(nums, start, right, k)
        elif k >= left:
            self.qsort(nums, left, end, k)