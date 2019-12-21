class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.find(nums1, nums2, n // 2 + 1)
        else:
            return (self.find(nums1, nums2, n // 2) + self.find(nums1, nums2, n // 2 + 1)) / 2
        
        
    def find(self, a, b, k):
        if not a:
            return b[k - 1]
        if not b:
            return a[k - 1]
        if k == 1:
            return min(a[0], b[0])
        tar_k = k // 2
        if len(a) >= tar_k:
            tar_a = a[tar_k - 1]
        else:
            tar_a = float('inf')
            
        if len(b) >= tar_k:
            tar_b = b[tar_k - 1]
        else: 
            tar_b = float('inf')
        
        if tar_a < tar_b:
            return self.find(a[tar_k:], b, k - tar_k)
        else:
            return self.find(a, b[tar_k:], k - tar_k)
        