class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if not A:
            return A
        ans = []
        for start in range(len(A) - 1, 0, -1):
            for i in range(start, 0, -1):
                if A[i] > A[0]:
                    A[: i + 1] = A[: i + 1][::-1]
                    ans.append(i + 1)
            A[: start + 1] = A[: start + 1][::-1]
            ans.append(start + 1)
            
        
        return ans
    
    

                    
        