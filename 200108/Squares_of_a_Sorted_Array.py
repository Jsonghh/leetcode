class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        first_natural = 0
        for idx, num in enumerate(A):
            if num >= 0:
                first_natural = idx
                break
        neg_idx, nat_idx = first_natural - 1, first_natural
        ans = []
        while neg_idx >= 0 and nat_idx < len(A):
            if A[neg_idx] ** 2 < A[nat_idx] ** 2:
                ans.append(A[neg_idx] ** 2)
                neg_idx -= 1
            else:
                ans.append(A[nat_idx] ** 2)
                nat_idx += 1
        while neg_idx >= 0:
            ans.append(A[neg_idx] ** 2)
            neg_idx -= 1
        while nat_idx < len(A):
            ans.append(A[nat_idx] ** 2)
            nat_idx += 1
        return ans
            
                
                
        