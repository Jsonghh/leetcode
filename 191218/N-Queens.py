class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # in which col(s), diagonal and antidiagonal Q has been placed
        col = set()
        dia = set()
        antidi = set()
        se_ans = [] # [[]] - > [2,1,0], row:idx, col:val
        self.helper(n, col, dia, antidi, [], se_ans)
        ans = self.get_ans(se_ans)
        return ans
    
    
    def helper(self, n, col, dia, antidi, cur, se_ans):
        if len(cur) == n:
            se_ans.append(cur[:])
            return
        
        row = len(cur)
        for coll in range(n):
            sum_, diff = row + coll, row - coll
            if coll in col or sum_ in dia or diff in antidi:
                continue
            cur.append(coll)
            col.add(coll)
            dia.add(sum_)
            antidi.add(diff)
            self.helper(n, col, dia, antidi, cur, se_ans)
            cur.pop()
            antidi.remove(diff)
            dia.remove(sum_)
            col.remove(coll)
    
    def get_ans(self, se_ans):
        #  [1,0]
        #  ['.Q',
        #  'Q,']
        ans = []
        for solution in se_ans:
            tmp = ['.'] * len(solution)
            cur_ans = []
            for col in solution:
                tmp[col] = 'Q'
                cur_ans.append(''.join(tmp))
                tmp[col] = '.'
            ans.append(cur_ans)
        return ans
                
            
            
        
        
        
        