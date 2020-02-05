class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for pos in range(len(words) - 1):
            is_valid, comp_len = True, True
            
            for i in range(min(len(words[pos]), len(words[pos + 1]))):
                pre, last = words[pos][i], words[pos + 1][i]
                if order.index(pre) < order.index(last):
                    is_valid = True
                    comp_len = False
                    break
                if order.index(pre) > order.index(last):
                    is_valid = False
                    comp_len = False
                    break
                    
            if comp_len:
                is_valid = len(words[pos]) < len(words[pos + 1])
                
            if not is_valid:
                return False 
            
        return True
        