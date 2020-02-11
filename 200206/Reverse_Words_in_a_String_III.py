class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        
        for idx, word in enumerate(s):
            s[idx] = ''.join(reversed(word))
            
        return ' '.join(s)
    
    
