from collections import Counter
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0
        if len(A) != len(B):
            return -1
        cnt_a, cnt_b = Counter(A), Counter(B)
        check_list = []
        for num, freq in cnt_a.items():
            check_list.append((freq, num, 'a'))
        for num, freq in cnt_b.items():
            check_list.append((freq, num, 'b'))
        check_list.sort(reverse=True)
        cnt = 0
        for freq, target, lst in check_list:
            if lst == 'a':
                to_list, from_list = A, B
            else:
                to_list, from_list = B, A
            invalid = False
            for i in range(len(A)):
                
                if to_list[i] == target:
                    continue
                if from_list[i] != target:
                    invalid = True
                    break
                cnt += 1
            if not invalid:
                return cnt
        return -1
                
                    
        
        