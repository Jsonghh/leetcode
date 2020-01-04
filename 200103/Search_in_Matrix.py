class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            i, j = mid // n, mid % n
            if matrix[i][j] < target:
                l = mid
            else:
                r = mid
        i1, j1 = l // n, l % n
        i2, j2 = r // n, r % n
        if matrix[i1][j1] == target or matrix[i2][j2] == target:
            return True
        return False
        
        